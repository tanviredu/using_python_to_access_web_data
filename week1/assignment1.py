
### importing the regular expression module

import re
def main():
    sum = 0
    fname = input("ENter the file name :")
    if len(fname) < 1:
        fname = "regex_sum_97406.txt"

    ## open the file
    handler = open(fname,'r')
    for line in handler:
        # print everyline
        #print(line)
        ## search for numbers with regular expression
        ## '[0-9]+' number from 0 to 9 and more
        numbers = re.findall('[0-9]+',line)

        if not numbers:
            continue
        else:
            ## summing all the number
            for number in numbers:
                sum+=int(number)

    print(sum)




main()
