"""
We need to convert romanStr Numerals to Integers
Much of this program is notes + extra for NCT personal knowledge.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Ex: III = 3
    IV = 4
    LVIII = 58
    MCMXCIV = 1994
    MMMCMLXXXVI = 3986
                              (C < M)   so we subtract C from M as a single value.
        (M+M+M)             + {M - C)    + L  + (X+X+X)    + V + I
        (1000+1000+1000)    + (1000-100) + 50 + (10+10+10) + 5 + 1

                            M       + C     + M
                            1000    + 100   + 1000 but C is less than M so we go M - C
                            1000    + (1000 - 100)

"""

class Solution():

    def roman2integer(self, romanStr):
        print("\n------------------------------------")
        print(f'romanStr = {romanStr}')
        # ------
        romanDict = {"I": 1,       # Create dictionary: romanStr:int
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}

        # for key in romanDict.keys():   # print out the full dictionary. not needed, just for show.
        #     value = romanDict[key]
        #     print(f'{key} = {value}')
        print("\n------------------------------------")

        # Remember that value for a key can be found if dict[key] exists.
        # EX. Is M a key in the dict, if so, what is M's value?
        total = 0
        # -------------------------------------------------------------------------------------

        for x in range(0, len(romanStr)):
            if x == len(romanStr)-1:  # Make sure break on the last one since, we don't want[x+1]
                print(f'x = {x}'
                      f'\nromanStr = {romanStr}')
                print(f'romanDict[romanStr[x]] = {romanStr[x]} =  {romanDict[romanStr[x]]}')
                total = total + romanDict[romanStr[x]]
                print(f'Last Value:     Total_if = {total}\n')
                break
            # -------------------------------------------------------------------------------------
            elif x != 0 and romanDict[romanStr[x]] > romanDict[romanStr[x-1]]:
                print(f'x = {x}'
                      f'\nromanStr = {romanStr}')
                print(f'PASS - romanDict[romanStr[x]] = {romanStr[x]} =  {romanDict[romanStr[x]]}\n')
                pass  # Skip spot 0, and ex. CM. Next elif will get this, we don't want to add the M again.
            # -------------------------------------------------------------------------------------
            elif romanDict[romanStr[x]] < romanDict[romanStr[x+1]]:  # Example (CM) = (1000 - 100)
                print(f'x = {x}'
                      f'\nromanStr = {romanStr}')
                print(f'romanDict[romanStr[x]] = {romanStr[x]} =  {romanDict[romanStr[x]]}')
                total = total + (romanDict[romanStr[x+1]] - romanDict[romanStr[x]])
                print(f'{romanStr[x+1]} - {romanStr[x]} = Total_elif2 = {total}\n')
            # -------------------------------------------------------------------------------------

            else:   # Not a subtraction combo, just add the value.
                print(f'x = {x}'
                      f'\nromanStr = {romanStr}')
                print(f'romanDict[romanStr[x]] = {romanStr[x]} = {romanDict[romanStr[x]]}')
                total = total + romanDict[romanStr[x]]
                print(f'Total_else = {total}\n')
            # -------------------------------------------------------------------------------------
        print(f'total = {total}')


try1 = Solution()
try1.roman2integer("MMMCMLXXXVI")
"""
M       M       M       M-C       L     X   X    X    V   I
1000 + 1000 + 1000 + (1000-100) + 50 + 10 + 10 + 10 + 5 + 1 = 3986
"""

#try1.roman2integer("MCMXCVI")
"""
1000 + (1000 - 100) + (100 - 10) + 5 + 1    = 1996
1000 + 900          + 90         + 5 + 1
"""

