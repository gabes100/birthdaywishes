# Birthday Wishes
A python application that automagically wishes your friends and family a birthday wish so you don't have to. This is work in progress so expect some bugs
### Dependances
- Selenium
### Pre-Setup
- Make sure selenium is installed globally or in a virtualenv. `pip3 install selenium` will do the trick globally
- Chrome driver must be in PATH. Driver depends of OS. Can be found at https://chromedriver.chromium.org/downloads
- Make sure you have a valid gmail address to be able to login and send email. What I did for that is I created a new gmail account and turned on
"Less secure app access" this will allow python to login into that gmail and send the info to your personal email address
### Setup
##### config.ini
- Edit `config.ini` to match email credentials and facebook login credentials
##### people.csv
- Edit `people.csv`to list available birthdays on facebook
- The format for a person goes as follows:
birthday,firstname,lastname,action,nickname(optional)<br/>
an example of that would look like
01/01,John,Doe,1
- There is chrome extension that will pull this data from facebook. This is something that will be reworked in the future
