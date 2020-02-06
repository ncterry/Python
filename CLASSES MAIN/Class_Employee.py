import sys
import os
# ---------------------------------------------------
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # This email will work, but if we change the first, the email won't pick it up.
        # self.email = self.first + '.' + self.last + '@email.com'
        # Need to use the property decorator
    @property
    def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #if we want to set Employee fullname by:
        #   emp_1 = Employee('John', 'Smith')
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    #If we call this both the first and last will be set to null
    @fullname.deleter
    def fullname(self):
        print("Gonna Delete")
        self.first = None
        self.last = None
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print("We created the employee John Smith, then changed the first to Jim")
print("This changes the first, but does not translate to the email.")
print("We need to include the @propery decorator in the class")
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print("We need special set function to changed everything for the Employee")
print("We will be using the 'Property Decorator'")



print("\nWe just used the property decorator in the class to set a full name at once.")
emp_1.fullname = 'Nate Terry'
print(emp_1.fullname)


print("\nWe just used the property decorator to delete the objects full name at once ")
del emp_1.fullname
print(emp_1.fullname)