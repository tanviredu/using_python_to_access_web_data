## this is a simple spyder 
## webparser program
## it will fetch the given url
## then fetch all the url
## inside this page has
import urllib.request as ur
from bs4 import *


current_repeat_count = 0
url = input("Enter url \n >")
if len(url) <1:
    url = "http://py4e-data.dr-chuck.net/known_by_Annick.html"
repeat_count = int(input("Enter Count : \n>"))
position = int(input("Enter position: \n>"))


def parse(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    ## find all the link in "<a>" tag
    tags = soup('a')
    #print(tags)
    return tags
    ## now we get the all the tags the websire got



while current_repeat_count < repeat_count:
    print("Retrieving: ",url)
    tags = parse(url)
    ## loop through all the tages with index
    for index,item in enumerate(tags):
        ## so this 'item' in the loop
        ## is a bs4 element
        if index == position -1:
            ## if index matchs the posion number
            ## then it will fetch the url data
            ## so it will search for link in a data
            ## as long time as you tell
            ## and when your target number 
            ## matches it will fetch the url
            ## asign the url to the url variable
            ## and parse it witin a while loop
            url = item.get('href',None)
            name = item.contents[0]
            # print(name)
            break
        else:
            continue
    current_repeat_count +=1

print("Last Url: ",url)
