#!/usr/bin/env python3


import os, json
print("Content-type:text/html\r\n\r\n")
print("<title>CGI Lab</title>")

# # Q1 - access environment variables with os.environ
# print(os.environ)
env_json = json.dumps(dict(os.environ), indent=4)
# print(env_json)

# Q2 - QUERY_STRING environ variable stores the URL query string
for param in os.environ.keys():
    if param == "QUERY_STRING":
        print("<b>{}: </b><span>{}</span><br>".format(param, os.environ[param]))

# Q3 - contains information about the user’s browser?
for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("<b>{}: </b><span>{}</span><br>".format(param, os.environ[param]))