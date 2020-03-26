import urllib.request as ur
import xml.etree.ElementTree as et

url = input("Enter Url \n>")
if len(url) <1:
    url = "http://py4e-data.dr-chuck.net/comments_97410.xml"

total_number = 0
total_sum = 0
print("Retrevieng Url" ,url)

xml = ur.urlopen(url).read()
print("Retreve {} character",format(len(xml)))
tree = et.fromstring(xml)
print(tree) ## its a tree object


# these are the shape of the tree
#<comments>
#    <comment>
#       <name>Shiloh</name>
#       <count>100</count>
#    </comment>

counts = tree.findall('.//count')
## just like the tree it is has two upper branch
## 1) comments
## 2) comment
## thats why .//count
##print(counts)

for count in counts:
    total_sum+=int(count.text)
    total_number+=1

print('Count: ',total_number)
print("Sum:",total_sum)

