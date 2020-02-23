"""
Write a function to check if a string is a palindrome or not.
"""
# ------------------------------------------------------------------------------
# Same functions, but the first one is clean without comments, and prints.
# Note - these are based on a default python code, not imported methods
def clean_palindrome(thestring):
    end = len(thestring) - 1
    same = True
    while same:
        for x in range(0, round(len(thestring)/2) + 1):
            if x == end:  # madam
                print("Reached the middle. This is a Palindrome")
                same = False; break
            elif x + 1 == end and len(thestring) % 2 == 0:  # maam
                print("Reached the middle. This is a Palindrome")
                same = False; break
            elif thestring[x] != thestring[end]:  # 'x' moves to x+1 and 'end' moves to "end-1" until x=end
                print("Not a Palindrome")
                same = False; break  # If wrong, break-for-loop, and stop-while-True
            end = end - 1
# ------------------------------------------------------------------------------

def palindrome(thestring):
    print("\n\n\n----------------------")
    print(f'String = {thestring}')
    print(f'Length = {len(thestring)}\n')
    print(f'round = {round(len(thestring)/2)}')
    #
    end = len(thestring)-1  # EX. Length=13, last-letter=12

    comparedict = {}        # Dict is just for pretty print at the end.
    same = True
    # ----------
    while same:  # Stay in loop while corresponding letters are the same.
        # Compare first half(starting at front) to the back half(starting at the end)
        for x in range(0, round(len(thestring) / 2)+1):     # "madam" = 5 --> 2.5 --> 2
            print(f'x = {x}')
            print(f'{thestring[x]}')
            print(f'end = {end}')
            print(f'{thestring[end]}')
            # ----------------------------------------------------------------------
            # Note: You can adjust the value of a key, but
            # You cannot append a key to a dict if that key already exists.
            #   key : value
            # nathanCnahtan - an C na - the last a,n will not be added, because they already exist as a key
            if x == end:
                print("Reached the middle. This is a Palindrome")
                comparedict[thestring[x]] = "Middle"
                same = False; break
            elif x+1 == end and len(thestring) % 2 == 0:
                print("Reached the middle. This is a Palindrome")
                comparedict[thestring[x]] = thestring[end]
                comparedict[" "] = "Middle"
                same = False; break
            # ----------------------------------------------------------------------
            elif thestring[x] != thestring[end]:          # 'x' moves to x+1 and 'end' moves to "end-1" until x=end
                print("Not a Palindrome")
                comparedict[thestring[x]] = thestring[end]
                same = False; break  # If wrong, break-for-loop, and stop-while-True
            else:
                comparedict[thestring[x]] = thestring[end]  # Dict just for print at the end.
            end = end-1
    # -----------------
    return comparedict
# End Function ---------------------------
# ----------------------------------------


forshow = palindrome("madam")
for key, value in forshow.items():
    print(f'{key} : {value}')
# ---------------------------------------
forshow = palindrome("maam")
for key, value in forshow.items():
    print(f'{key} : {value}')

# ---------------------------------------
print("\n\n\n-----------\nclean_palidrome + madam")
clean_palindrome("madam")

# ---------------------------------------
print("\n\n\n-----------\nclean_palidrome + maam")
clean_palindrome("maam")
# ---------------------------------------
