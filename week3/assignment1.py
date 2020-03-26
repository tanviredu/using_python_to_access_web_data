## for getting web data
import urllib.request as ur
## parsing html
from bs4 import *

url = input("Enter url to scrape ..\n>")
if len(url) <1:
    url = "http://py4e-data.dr-chuck.net/comments_97408.html"
print (url)
## get the html data
html = ur.urlopen(url)
## all the html data will be stored here
html = html.read()

## parse it
soup = BeautifulSoup(html,'html.parser')
#print(soup)
## we will find the span and count it
count_span = 0
value_sum = 0

spans = soup('span') ## this will return all the result including span

for span in spans:
    #print(span)
    #print(span.contents)
    # it will give the element in a list
    # so we take the first element
    value = int(span.contents[0])
    value_sum+=value
    count_span+=1
    
## it will show something like  this
#<span class="comments">97</span>
#<span class="comments">97</span>
#<span class="comments">96</span>
#<span class="comments">94</span>
#<span class="comments">94</span>
#<span class="comments">94</span>

print('Count ',count_span)
print('Sum ',value_sum)
