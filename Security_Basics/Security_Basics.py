
''' Know that python can be placed into a file such as:

    import <module1>, <module2>
    def myFunction():
    def main():
        myFunction()

    Python does force indentation, even if you write in a seperate file.
        Seen specifically on loops, if/elif/else, etc.


        '''

print('\nString basics:   ')
domain = 'google.com'
print(domain)
print(domain[0])
print(domain[0:3])
print(domain[1:])
print(len(domain))


print('\n\n Integers')
a =1
b =2
print(a+b)
print(a*b)


print('\n\n Lists')

string1 = 'how:are:you:doing:?'
list1 = string1.split(':')
print('The string = ', string1)
print('The list from:  string1.split(\':\') = \n\t', list1)


list2 = ['8.8.8.8', '53']
print('\n list2 = ', list2)
print('\t list2[0] = ', list2[0])
print('\t list2.append(\'google\') = ')
list2.append('google')
print('\t\t', list2)
print('\t list2.remove(\'google\')')
list2.remove('google')
print('\t\t', list2)


print('The help function will display details:    help(type) = ')
print(help(type))
print('*****YOU CAN SEE THERE IS A LOT OF INFORMATION ABOVE\n\n')



print('****************************************')
ip = "We want help on how to split this string."
print(ip)
print(help(ip.split))





print('****************************************')
print('Simple If then example for a domain name.')
domain = 'google.com'
if domain == 'yahoo.com':
    print('\tDo nothing.')
elif domain == 'google.com':
    print('\tFound it. Do Hack')
else:
    print('\tNo Go.')


print('\n\n****************************************')
''' As you write python code, you will hit errors such as:
    * Can't connect to the host
    * Syntax error
    * No data is returned from a particular function.
    * Etc
    To handle these errors, use try/Except'''
try:
    s.connect(('127.0.0.1', 23))
except: pass



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

'''alsdf We are stuck here, the last program goes through, but when it spits back the
data it received, it is not the "Happy Hacking" that we send. it is empty.'''
print('\n\n****************************************')

print('\n\n****************************************')

print('\n\n****************************************')

print('\n\n****************************************')

print('\n\n****************************************')

print('\n\n****************************************')





