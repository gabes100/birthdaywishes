#!/usr/bin/python3

import csv

from datetime import datetime
from friend import Friend
import mail
import facebook

def main():
    file_name = "people.csv"
    friends = read_file(file_name)
    now = datetime.now()

    # Get birthdays for each action
    facebook_list = [f for f in friends if ((f.getAction() == 1 or f.getAction() == 2 or f.getAction() == 4) and check_birthday(now, f))]
    mail_list = [f for f in friends if ((f.getAction() == 1 or f.getAction() >= 3) and check_birthday(now, f))]

    #send facebook birthdays
    auto_send_ret = facebook.sendMessage(facebook_list)

    # send info to self
    mail.sendMail(mail_list, auto_send_ret)

def read_file(file_in):
    friends = []
    with open(file_in, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if len(row) == 4:
                f = Friend(row[0], row[1], row[2], row[3])
                friends.append(f)
            else:
                f = Friend(row[0], row[1], row[2], row[3], row[4])
                friends.append(f)

    return friends


def check_birthday(tdate, person):
    month = tdate.strftime("%m")
    day = tdate.strftime("%d")
    if person.getBmonth() == month:
        if person.getBday() == day:
            return True
    else:
        return False

if __name__ == '__main__':
    main()
