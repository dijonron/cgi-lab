#!/usr/bin/env python3

import cgi, cgitb

# field storage so we can access form inputs
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')


# report posted values
print("Content-type:text/html\r\n\r\n")
print("<title>POSTed data</title>")
print("<b>USERNAME: </b><span>{}</span><br><b>PASSWORD: </b><span>{}</span><br>".format(username, password))