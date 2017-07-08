print('\n\n****************************************')
''' Python Socket Objects: are just like files, you can read and write to them.
These are the entry point for sending and receiving data to a client.

Python -> Clients Job:
    connect --> send --> receive
'''
print(' Example of a simple client:')
'''localhost is our computer, to find an open port:
        cmd+space --> Search "Network Utility
            Click: "Port Scan
                Open Port Search in: 127.0.0.1
    It will return a list of open ports on your computer.'''

# mini client program
# Make sure miniserver.py is running
import socket
# create a socket, in a TCP/IP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# created above, now get it to do something.
s.connect(('localhost', 5037))
# We are sending this statement, but we open in binary, so have to send in binary.
s.send(b'Happy Hacking')
# have to indicate that data was received, and can specify how much. Here 1024 bytes
# This will return, what the port has received.
data = s.recv(1024)

s.close()
print('Received:')
print(data)