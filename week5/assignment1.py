## same as xml but only json format
import urllib.request as ur
import json

json_url = input("Enter location: \n>")
if len(json_url) <1:
    json_url = "http://python-data.dr-chuck.net/comments_42.json"
print("Retrieving ",json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print("Retrieved {} characters",format(len(data)))
json_obj = json.loads(data)


total_sum = 0
total_number = 0

for comment in json_obj["comments"]:
    total_sum +=int((comment['count']))
    total_number+=1
print("Count:",total_number)
print("Sum:",total_sum)
