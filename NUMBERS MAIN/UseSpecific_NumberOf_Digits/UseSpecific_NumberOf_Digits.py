# ===============================================================
# ===============================================================
print('\n\n')
# This will print values 1 - 10 same as: (for(int i=1; i<11; i++)
for i in range(1,11):
    sentence8 = 'The value is {}'.format(i)
    print(sentence8)

# Same thing but we want to automatically pad 2digits  so 2 will be 02
print('---------------')
# Include :02 in the {} to say we want TWO digits guaranteed.
for i in range(1,11):
    sentence8 = 'The value is {:02}'.format(i)
    print(sentence8)

# Same thing but we want to automatically pad 3digits  so 2 will be 002
print('---------------')
# Include :03 in the {} to say we want THREE digits guaranteed.
for i in range(1,11):
    sentence8 = 'The value is {:03}'.format(i)
    print(sentence8)
# ===============================================================
# ===============================================================

# ===============================================================
# ===============================================================
print('\n\n')
print('How to print out a specific number of decimal places.')
pi = 3.14159265
sentencePi = 'Pi is equal to {:.3f}'.format(pi)
print(sentencePi)
sentencePi = 'Pi is equal to {:.6f}'.format(pi)
print(sentencePi)
# ===============================================================
# ===============================================================


# ===============================================================
# ===============================================================
# Print out a large number with comma seperators
print('\n\n')

print('A number using a comma to seperate the digits at a location.')
sentenceSeperate = '1MB is equal to {:,} bytes'.format(1000**2)
print(sentenceSeperate)
print('---------------')
print('A number using a comma to seperate the digits at a location, and add decimal distinction.')
sentenceSeperate = '1MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentenceSeperate)
# ===============================================================
