
print('\n\n This is a common interview question.')
print(' Go through the list. \n if number is divisible by 3 print Fizz')
print(' If number is divisible by 5, print Buzz')
print(' If number is divisible by both, print FizzBuzz')


print('\n\n Remember, more specific at the top.')
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('\t', number, ' FizzBuzz')
    elif number % 3 == 0:
        print('\t', number, ' Fizz')
    elif number % 5 == 0:
        print('\t', number, ' Buzz')

    else:
        print(number, ' is not divisible by 3 or 5')