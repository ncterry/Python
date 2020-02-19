# Reverse a string through a function
def reverse(string_in):
    string_out = ""
    for c in string_in:
        string_out = c + string_out
        print(string_out)

    return string_out

reverse("Nathan")
'''
N
aN
taN
htaN
ahtaN
nahtaN
nahtaN
'''