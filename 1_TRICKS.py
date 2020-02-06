
newline = "\n---------------"
print(newline + "Trick 1") # ============
print("You can use underscores in numbers, in place of commas."
      "\nThis will not affect an integer:  10_000_000_000")

n1 = 10_000_000_000
n2 = 1_000_000
print(f'10_000_000_000 '
      f'\n+    1_000_000 \nTotal = {n1 + n2}')
print(f'\nAND you can add commas to print:')
print("\'{Total:,}\' = ")
print(f'{(n1 + n2):,}')
'''
10_000_000_000 
+    1_000_000 
Total = 10001000000

AND you can add commas to print:
'{Total:,}' = 
10,001,000,000

'''
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 2") # ============
print("Change if/else condition into 1 line")
condition = True
# Normal Setup
if condition:
    x = 1
else:
    x = 0
# -----------------------
# Single line
# X=1 if condition is true, else x=0
x = 1 if condition else 0
print(f'x = {x}')
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 3") # ============
print("Context Managers - Google for more info")
print("Function open/close files.")
# Normal
# fyle = open('TRICKS.txt', 'r')
# file_contents = fyle.read()
# fyle.close()
# -------------------------
# Faster Function
# Opens file, then auto-closes after loop.
with open("TRICKS.txt", 'r') as f:
    file_contents = f.read()


words = file_contents.split(' ')
word_count = len(words)
print(f'Word count = {word_count}')

# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 4") # ============
print("Enumerator count")
names = ['Corey', 'Chris', 'Dave', 'Travis']
# Normal:
# Start with index, and increase each loop.
# index=0  --> index += 1      Works but is sloppy
# Better:
for index, name in enumerate(names, start=1):
    print(index, name)
'''
1 Corey
2 Chris
3 Dave
4 Travis
'''

# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 5") # ============
print("Enumerator count with 2 lists")
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for index, name in enumerate(names):
    print(f'{name} is actually {heroes[index]}')
'''
Peter Parker is actually Spiderman
Clark Kent is actually Superman
Wade Wilson is actually Deadpool
Bruce Wayne is actually Batman
'''
# ----------------------------------
print(newline)
print("Second option:")
# Note: ZIP will end at the shortest list.
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')
'''
Peter Parker is actually Spiderman from Marvel
Clark Kent is actually Superman from DC
Wade Wilson is actually Deadpool from Marvel
Bruce Wayne is actually Batman from DC
'''
# ----------------------------------
print(newline)
print("Third option:")
for values in zip(names, heroes, universes):
    print(values)
'''
('Peter Parker', 'Spiderman', 'Marvel')
('Clark Kent', 'Superman', 'DC')
('Wade Wilson', 'Deadpool', 'Marvel')
('Bruce Wayne', 'Batman', 'DC')
'''
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 6") # ============
print("Unpacking...")
print("What if we import a list, but only need the first value."
      "\nWe will get an error, if we don't catch the second value."
      "\nAdd an underscore, and it will negate the second value.")
a, _ = (1, 2)
print("a, _ = (1, 2)")
print(f'a = {a}')
# a = 1
# ---------------------
print(newline)
print("Set extras on an import to a spare Var")
print("Catch a and b, and set c to catch all the rest")
print("a, b, *c = [1, 2, 3, 4, 5]")
a, b, *c = [1, 2, 3, 4, 5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
'''
a = 1
b = 2
c = [3, 4, 5]

'''
# ---------------------
print(newline)
print("Set extras on an import to a spare Var example 2")
a, b, *c, d = [1, 2, 3, 4, 5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
'''
a = 1
b = 2
c = [3, 4]
d = 5

'''
# ---------------------
print(newline)
print("Set extras on an import to a spare Var example 3")
print("Ignore import values")
a, b, *_, d = [1, 2, 3, 4, 5, 6, 7]
print(f'a = {a}')
print(f'b = {b}')
#print(f'c = {c}')
print(f'd = {d}')
'''
a = 1
b = 2
d = 7

'''
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline + "Trick 7") # ============
print("Run this program from Terminal:  # python TRICKS.py"
      "\nWhen it asks for password, we want that hidden.")
print("For the password, instead of  input  use  getpass.")
from getpass import getpass
username = input("Username: ")
password = getpass("Password: ") # In terminal we don't want a shoulder surfer seeing the password.
# getpass does not work in pycharm. Only in Terminal. Shows a Key Symbol

print("Logging in....")
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline) # ============


# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline) # ============


# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline) # ============


# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline) # ============


# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
# ===========================
print(newline) # ============
