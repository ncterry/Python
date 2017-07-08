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
# ===============================================================
