# Prompt user for input
user = int(input())

#define function mass to joules conversion
def masstojoules(x):
#variable num holds placement for conversion
    num = x * 90000000000000000
#return the conversion result
    return num
#call function within a print statement
print(masstojoules(user))