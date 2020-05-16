"""
Given a list of daily temperatures, return a list such that for each day
    the return tells you how many days you have to wait to get a warmer temp.
    If there is no day in the future that is warmer, put 0

    EX. T = [73, 74, 75, 71, 69, 72, 76, 73]
    Return= [1,  1,  4,  2,  1,  1,  0,  0]

    Length of list  is from   [1, 30000]
    Temps from:    [30, 100]
"""
from random import randint  # To create a random list length, and random temps

class Solution(object):

    def createTempList(self):   # Function not needed but lets us create new random list each time.
        originaltemps = []
        for i in range(1, randint(2, 30000)):         # List random length between 2-30000
            originaltemps.append(randint(30, 100))  # Each temp random between 30-100
            #
        return originaltemps  # Return list of temps for day differences function to use.

    def dailyTemps(self, temps):
        originaldays = []   # How many days until next highest temp in list.
        for i in range(0, len(temps)):
            next = 0        # Move for the next day from i that has a higher temp.
            while True:     # Everything breaks out
                next += 1   # Start 1 spot past i in list
                if i + next == len(temps):  # Don't go past end of list.
                    originaldays.append(0)  # If we hit end of list, then no higher temp was found.
                    break
                    #
                elif temps[i] < temps[i + next]:  # Higher temp found, then append day count between days
                    originaldays.append(next)
                    break
                    #
        return temps, originaldays


try1 = Solution()
temps, dayslist = (try1.dailyTemps(try1.createTempList()))
# Prints below are just for show.
print(temps)
print(dayslist)
print(len(temps))
print(len(dayslist))
for n in range(len(temps)-1):
    print(f'{temps[n]} : {dayslist[n]}')
