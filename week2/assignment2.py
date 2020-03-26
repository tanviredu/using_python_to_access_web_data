## this is some basic socket programming
## its verty easy 
## it start with importing socket

import socket
import time

def main():
    ## create the socket object
    mysock = socket.socket()
    ## connect to the server
    ## the address and the port must be  a tuple
    mysock.connect(('data.pr4e.org',80))
    ## make the get request
    request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

    ## send the get request
    print("Sending request .........")
    time.sleep(2)
    mysock.send(request)
    print("sent....OK")
    time.sleep(2)
    ## enter a forever loop
    while True:
        ## getting the response
        print("Reciving ....")
        time.sleep(3)
        data = mysock.recv(512)
        if len(data) <1:
            break
        else:
            print(data.decode(),end="")
    mysock.close()
main()
