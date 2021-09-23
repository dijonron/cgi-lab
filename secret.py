#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
cgitb.enable()

class FollowingTheTAsInstructionsError(Exception):
    def __init__(self):
        Exception.__init__(self, (
            "You must edit secret.py to change the username, password, "
            "and to delete this error!"
        ))


# Edit the following two lines:
username = "dalton"
password = "cmput404"

form = cgi.FieldStorage()
post_username = form.getvalue('username')
post_password = form.getvalue('password')

if username == post_username and password == post_password:
    # if login correct, set cookie
    print ("Set-Cookie:Username = {};".format(post_username))
    print ("Set-Cookie:Password = {};".format(post_password))
    print ("Content-type:text/html\r\n\r\n")
    # use meta refresh to redirect back to login page
    # https://en.wikipedia.org/wiki/Meta_refresh
    print('<meta http-equiv="refresh" content="1; url=/login.py">')
else:
    # do not set cookies, just redirect back
    # use meta refresh to redirect back to login page
    # https://en.wikipedia.org/wiki/Meta_refresh
    print ("Content-type:text/html\r\n\r\n")
    print('<meta http-equiv="refresh" content="1; url=/login.py">')
