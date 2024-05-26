import smtplib, ssl
import os

port = 465
smtp_server ="smtp.gmail.com"
USERNAME = os.environ.get('USER_MAIL')
PASSWORD = os.environ.get('USER_PASSWORD')

message = """\
Subject: GitHub Email Report

This is your daily email report.

"""
context = ssl.create_default_context

with smtplib.SMPT_SSL(smtp_server, port, context=context) as serve :
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,USERNAME, message)