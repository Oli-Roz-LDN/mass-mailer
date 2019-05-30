# -*- coding: utf-8 -*-
"""
Author: Matt Robillard <matt@mattrobillard.us>
Version: 2019-05-28

Usage: $ mass_mailer.py [--dry-run] <mailserver.cfg> <emails.csv> <mail.html|txt>

Sends an individualized version of mail.html|txt to all recipient email
addresses contained in emails.csv; Configuration of the mail server is 
read from mailserver.cfg. Note that the mail server must support 

The configuration file, mailserver.cfg, has the following required fields:
  SMTP=smtp.gmail.com
  FROM=name@domain.com 
  SUBJECT=This is the subject
The following are optional fields:
  REPLY-TO=name@domain.com (defaults to FROM address)
  BCC=someone-to-bcc@domain.com

The mail.html|txt file may contain HTML markup and should be saved in UTF-8
encoding; A template ending with extension ".txt" triggers sending of plain text emails.

Email addresses should be given in comma-separated list form, e.g.:
  emails, city, phone
  john@domain.com
  noname@example.org
Given that there is a column titled 'emails', the emails will be extracted
correctly. 

You can use the optional "--dry-run" flag to run the script in testing mode
which will do everything except sending out the actual emails.
"""

import smtplib, ssl

port = 465  # for SSL
smtp_server = "smtp.gmail.com"
sender_email = "contact@akordhomes.com" 
receiver_email = "robillard.matt@gmail.com" 
password = input("Type your password and press enter: ")
message = """\
From: contact@akordhomes.com\n\
To: robillard.matt@gmail.com\n\
Subject: Real Estate Market Survey\n\


This message is sent from Python.\

Best, 

Matt
Co-founder
"""

def send_email():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)
    server.set_debuglevel(1)
    server.sendmail(
      sender_email, 
      receiver_email, 
      message)
    server.quit()
