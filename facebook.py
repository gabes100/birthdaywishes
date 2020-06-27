import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import configparser

def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False

def sendMessage(facebook_list):
    if len(facebook_list) < 1:
        return "Nobody's birthday is today :("

    config=configparser.ConfigParser()
    config.read("config.ini")
    error_message = ""

    # Setup driver and go to Facebook
    try:
        # set options
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        options.headless = str_to_bool(config['DEBUG']['chrome_headless'])

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.facebook.com/')
    except:
        error_message = "Error trying to go to Facebook"
        return error_message

    # login
    try:
        username = config['FACEBOOK']['email']
        password = config['FACEBOOK']['pass']

        element = driver.find_elements_by_xpath('//*[@id ="email"]')
        element[0].send_keys(username)

        element = driver.find_element_by_xpath('//*[@id ="pass"]')
        element.send_keys(password)

        log_in = driver.find_elements_by_id('loginbutton')
        log_in[0].click()
    except:
        driver.close()
        error_message = "Error logging into Facebook"
        return error_message

    # Make sure elements load
    driver.implicitly_wait(5)
    time.sleep(10)

    # Wish birthdays
    try:
        driver.get("https://www.facebook.com/events/birthdays/")

        driver.implicitly_wait(5)
        response = 'Happy Birthday!!'

        for person in facebook_list:
            person_elems=driver.find_elements_by_xpath("//a[@title='" + person.getFullName() + "']/../../..//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")

            if len(person_elems) > 0:
                person_elems[0].send_keys(response)
                person_elems[0].send_keys(Keys.RETURN)
                person.setMessage("Sent message on Facebook")
            else:
                person.setMessage("Did not send message")
    except:
        driver.close()
        error_message = "Error sending messages"
        return error_message

    time.sleep(5)
    driver.close()
    return "Success"
