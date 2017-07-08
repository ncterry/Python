'''First class function is what the program treats as a first class citizen or
a first class object. '''
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
print('\n Create a simple function. To return the square of a number')
def square(x):
    return x * x

print("\n Sets f = to the result of the square function")
print(' Run the function with a 5 = ')
f = square(5)
print(f)

print('\n print(square) = ')
print(square)
print(' We just printed a function itself without a value. Returns a random info')


print("\n Important: We can set a variable to be equal to the function itself")
g = square
print(g)
print(g(5))
print("Set g=function so now you can use g as the function.")
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
print('\n'*2)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# We are passing the function itself into the list
squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
def cube(x):
    return x * x * x

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)