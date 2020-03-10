
print(' The fibonacci interview question is pretty simple.')
print(' Standard fibonacci, create a program that prints the previous ')
print(' two numbers.')



# numbersprint(' Create a function.')
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for n in range(1, 101):
#     print(n, ":", fibonacci(n))
print('The function above works, but it will be very slow. ')


print('\n\n Use Memoization')
fibonacci_cache = {}
def fibonacci(n):
    # if we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return  value

for n in range(1,1001):
    print(n, ":", fibonacci(n))