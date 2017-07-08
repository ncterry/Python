import sys
import os


# Takes in a message argument
def logger(msg):
    # Does not take in anything. Just executes and prints with msg passed in.
    def log_message():
        print('Log:', msg)
    # Returning the Log: msg function.
    return log_message


'''set log_hi var equal to the logger function with 'Hi'
So now the log_hi variable is equal to the log_message function.
So now we can run that variable just like a function.
'''
log_hi = logger('Hi')
log_hi()




print("\nexample-------------------------------"*2)

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
# nothing is done yet. print_h1 just equals a function
print_h1('Test Headline!')
print_h1('Another Headline!')
# set it equal to a function, then ran it as the funtion.

print_p = html_tag('p')
print_p('Test Paragraph!')

