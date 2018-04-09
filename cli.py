#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys

s = socket.socket()         # Create a socket object
host = '127.0.0.1'     # Get local machine name
port = 5000              # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print 'sending "%s"' % message
    s.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = s.recv(20)
        amount_received += len(data)
        print 'received "%s"' % data
finally:

	s.close()                     # Close the socket when done