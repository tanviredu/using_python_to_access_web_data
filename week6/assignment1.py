import urllib.request as ur
import urllib.parse as up
import json
url  = "http://python-data.dr-chuck.net/geojson?"

address_input = input("Enter your location\n>")
## this are api parameter
params = {"sensor":"false","address":address_input}
url = url+up.urlencode(params)
## this will create a proper get string
#print(url)
print("Retrieving ",url)
data = ur.urlopen(url).read().decode('utf-8')
print("Retrieved {} characters".format(len(data)))

## it will send  a json too

json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id",place_id)
