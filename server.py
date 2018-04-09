#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 5005              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send('Thank you for connecting')

c.close()