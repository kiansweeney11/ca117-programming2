#!/usr/bin/env python


import re
date = r'\b\d?\d[-/]\d?\d[-/]\d\d\b'
phone = r'\b01[-\s]\d{7}\b'
email = r'\b[\w.]*@[\w.]*\w'
ldate = r'\b\d*\d .{3} \d\d'


from re import findall
import sys

from patterns_062 import date, phone, email, ldate

def main():

    # Verify regular expressions are not overly long
    assert(len(date) < 30)
    assert(len(phone) < 30)
    assert(len(email) < 40)
    assert(len(ldate) < 80)

    s = sys.stdin.read()

    datelist = findall(date, s)
    print('Dates: {}'.format(datelist))

    phonelist = findall(phone, s)
    print('Phones: {}'.format(phonelist))

    emaillist = findall(email, s)
    print('Emails: {}'.format(emaillist))

    ldatelist = findall(ldate, s)
    print('Long dates: {}'.format(ldatelist))

if __name__ == '__main__':
    main()
