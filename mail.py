import smtplib
import ssl
import configparser

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(birthday_list, auto_send_ret):
    config=configparser.ConfigParser()
    config.read("config.ini")

    FROM = config['EMAIL']['gmail_user']
    PASSWORD = config['EMAIL']['gmail_pass']

    TO = config['EMAIL']['email_receiver']
    SUBJECT = 'Daily Reminder Birthdays'

    message = MIMEMultipart("alternative")
    message["Subject"] = SUBJECT
    message["From"] = FROM
    message["To"] = TO

    html_start = "<html><body>"
    html_end = "</html></body>"

    birthday_table = """\
    <table style="border-collapse:collapse; border:none; vertical-align:top; margin:0px; width:100%">
        <tbody>
            <tr>
                <td align="left" style="padding:15px; background-color:rgb(15,85,88)">
                    <p style="font-family:&quot;roboto&quot;,helvetica,sans-serif; font-size:24px; color:rgb(255,255,255); margin:0px; font-weight:bold">Birthdays</p>
                    <p style="font-family:&quot;roboto&quot;,helvetica,sans-serif; font-size:16px; color:rgb(255,255,255); margin:0px; font-weight:bold">Facebook Status:</p>
                    <p style="font-family:&quot;roboto&quot;,helvetica,sans-serif; font-size:16px; color:rgb(255,255,255); margin:0px; font-weight:bold">"""
    birthday_table = birthday_table + auto_send_ret + "</p>"
    birthday_table = birthday_table + """\
                </td>
            </tr>
            <tr>
                <td align="left" style="padding:15px; color:rgb(232,232,232); background-color:rgb(25,135,139)">
                    <ul style="font-family:&quot;roboto&quot;,helvetica,sans-serif; font-size:20px; line-height:2">
                    """
    for e in birthday_list:
        birthday_table = birthday_table + "<li>" + e.getName() + " (" + e.getMessage() + ")" + "</li>"
    birthday_table = birthday_table + "</ul></td></tr><tr><td&nbsp;</td></tr></tbody></table>"

    HTML = html_start + birthday_table + html_end
    body = MIMEText(HTML, "html")
    message.attach(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(FROM, PASSWORD)
        server.sendmail(FROM, TO, message.as_string())

    return 0
