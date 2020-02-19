#!/bin/python3

newline = "\n-------------"
print(newline)

#Print String
print("Strings and things!")
print('Single quotes work also.')
print("""---------------------
Triple quotes
let us print on numerous lines.""")

print(newline)

#Concatenation
temp = "This is "
print(temp + "a new string combo")

print(newline)

#Basic Math
print("\nMath time:")
print("50+50 = " + str(50 + 50)) #add
print("50-49 = " + str(50 - 49)) #subtract
print("4*3 = " + str(4 * 3))   #multiply
print("5/2 = " + str(5 / 2))   #divide
print("50+50-49*2/4 = " + str(50 + 50 - 49 * 2 / 4)) #pemdas
print("50**2 = " + str(50 ** 2)) #power
print("50%3 = " + str(50 % 3))  #modulus/remainder 6*8  +2
print("50//2 = " + str(50 // 6)) #how many 6 goes into 50

print(newline)

#Variables and Methods
print("Fun with variables and methods.\n")
quote = "All is fair in love and war"
print("Quote = " + quote)
print("Length of quote = " + str(len(quote)))
print("uppercase = " + quote.upper())
print("lowercase = " + quote.lower())
print("title = " + quote.title())
print("\n\n")

name = "Nate" #string
age = 33  #int
gpa = 3.7 #float
print(name)
print(age)
print(name + str(age))
print("My name is " +name+ ", I am " +str(age)+ ", and my gpa was " +str(gpa))

#Increase age by 1
age += 1


#Create function for square root
def sqroot(x, y):
	return(x**y)

print("\n\nSquare root of 9 = " + str(sqroot(9, 0.5)))
