'''
If given an array with whole numbers,
    indicate if there are duplicates.

[1,2,3,3,4,6,7]     = 3
[1,2,3,4,5]         = any return

'''

# This is a base count with for loops. We do not use math imports
def find_duplicate(list=[], duplicates=[]):
    for n in range(0, len(list)):
        for x in range(n+1, len(list)):
            if list[n] == list[x]:
                duplicates.append(list[n])
    return duplicates

print(f'\n\nDuplicates = {find_duplicate([1,3,7,2,8,4,9,6,5,6,10,11,14,2,17,18], [])}')

# ==============================
# ==============================
# ==============================
# Use default python count function to count how many times item appears in list.
# for loop through list
# if count of value is more than 1 in 'list', AND has not already been appended to 'duplicates'
#           Just so final duplicates is   [2, 6]   NOT   [2, 6, 6, 2]
def count_duplicates(list=[], duplicates=[]):
    for n in list:
        if list.count(n) > 1 and duplicates.count(n) == 0:
            duplicates.append(n)
    return duplicates

# ==============================
# ==============================
# ==============================
# same thing but use dictionary for duplicates
# We can return the duplicates, and count how many times that they were duplciated
def total_duplicates(list=[], duplicates=[], dicts={}):
    for n in list:
        if list.count(n) > 1 and duplicates.count(n) == 0:
            duplicates.append(n)
            dicts[n] = list.count(n)
    return dicts




# -------------------------------------
print(f'\n\nCount Duplicates = {count_duplicates([1,3,7,2,8,4,9,6,5,6,10,11,14,2,17,18], [])}')
# -------------------------------------
print(f'\n\nCount Duplicates = {count_duplicates("noiwhjahf;k;nwainne;ah;fiwehjoihlcsnmo2398hf894h349ohjf9v0q23d08nbpq", [])}')
# -------------------------------------
# first print, just shows a line of duplicates/count
# the return value and for-loop print just looks prettier.
#print(f'\n\nTotal Duplicates = {total_duplicates("noiwhjahf;k;nwainne;ah;fiwehjoihlcsnmo2398hf894h349ohjf9v0q23d08nbpq", [], {})}')
dict_duplicates = total_duplicates("noiwhjahf;k;nwainne;ah;fiwehjoihlcsnmo2398hf894h349ohjf9v0q23d08nbpq", [], {})
for key, value in dict_duplicates.items():
    print(f'{key} : {value}')