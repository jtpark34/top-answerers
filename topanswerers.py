import json
from sys import argv
import requests

script, tag = argv
link = f"https://linkedin.stackenterprise.co/api/2.2/tags/{tag}/top-answerers/all_time?key=keyID"
request = requests.get(link)
data = request.json() # returns json result of get request

for i in data["items"]: # loops through dictionary "items"
    userdata = i["user"] # sets as variable the values for key "user"
    postcount = i["post_count"] # sets as variable the value for key "postcount"
    for x in [userdata]: # loops through each item in "user"
        print(x["display_name"], f"({postcount})") # prints value for key "display_name", and formatted string.
