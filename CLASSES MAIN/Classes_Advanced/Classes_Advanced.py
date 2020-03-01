
import sys
import os
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
# Created an employee class, with a constructor that requires first, last and pay
'''Note. For a standard class, 'self' will pass the object into the class
but with the class method, we are using the cls. There is also a static method
'''

#-------------------------------------------------
class Employee:
    raise_amount = 1.04  # built in yearly raise
    Num_Of_Emps = 0

    # -------------------------------------------------
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        '''The Num_Of_Emps is built into the actual class. Because
        we have set this to change with "Employee" and not "self"
        every time we create a new employee, the number will rise.
        Note I could not write this above the constructor'''
        Employee.Num_Of_Emps += 1

    # create a method within the class to print the full name
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    # -------------------------------------------------
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # -------------------------------------------------
    #   we use this @classmethod to raise the amount for all Employees
    #   used on line 98
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # -------------------------------------------------
    @classmethod  # Creating an alternative constructor with a dash string
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
    # Remem. the cls means we will use 'Employee' in front not an object
    # line 128 --> we can actually return a new Employee
    # -------------------------------------------------
    # This static class will accept a date and tell us if it is a workday or not
    @staticmethod       # use on line 145
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#-----------------------------------------------------------------    # Special Methods: NOTE Dunder = double + under
    '''Both repr and str are basically displays. repr is more techincal and for the programmer
        while str is more for a user. '''
    def __repr__(self):
        return "Employee('{}', '{}', '{})".format(self.first, self.last, self.pay)

# -----------------------------------------------------------------
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)
# -----------------------------------------------------------------
# __add__ is different int vs string. We can change that even more
# Wnen we add two employees together this is what it will return. The Pay
# Seen on line 134
    def __add__(self, other):
        return self.pay + other.pay
# -----------------------------------------------------------------
# __len__ is a built-in functino but we can overide it to deal with employees
# seen on line 152
    def __len__(self):
        return len(self.fullName())
# ------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 55325)

print("\n This is the standard __repr__ from the Employee class")
print(emp_1)
print(emp_1.email)
print("\n Here is the __repr__ and __str__ in the exact form.")
print("\t emp_1.__repr__() = ")
print("\t     ", emp_1.__repr__())
print("\t emp_1.__str__() = ")
print("\t     ", emp_1.__str__())
print("\t Both forms are based on the format dictated in the class.")



print("\nprint(1 + 2) uses the standard function 'add' which is different for int and string.")
print("print(1 + 2) = ")
print(1 + 2)
print("print('a' + 'b') = ")
print('a' + 'b')
print("These inherently use int vs string formats seen here:")
print("print(int.__add__(1,2)")
print(int.__add__(1,2))
print("print(str.__add__('a','b'))")
print(str.__add__('a','b'))



print("\nRemember there are different types of add that the computer knows,")
print("but it doesnt know how to add 2 employees. We overloaded the add function")
print("to be able to interprate adding two employees together")
print("print(emp_1 + emp_2) --> adds the salaries")
print(emp_1 + emp_2)


print("\nlength of a string in two ways")
print(len('test'))
print('test'.__len__())
print("Our over-ridden len function for an Employee")
print(len(emp_1))
print(emp_1.first, emp_1.last)