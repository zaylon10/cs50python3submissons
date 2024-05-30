# create infinite loop until condition is met.
while True:
    #prompt user for input.
    fuel = input("Fraction: ")
    #try block/split method/division to get desired outcome/ break once condition is met to return output.
    try:
        numerator , denominator = fuel.split("/")
        
        new_numerator = int(numerator)
        new_denominator = int(denominator)

        conversion = (new_numerator/ new_denominator)

        if conversion <= 1:
            break
    #exception handling.(pass until condition is met.)
    except(ValueError, ZeroDivisionError):
        pass
#multiply to convert.
percentage = conversion * 100
# branching to achieve desired outcome.
if percentage < 1:
    print("E")
elif percentage > 99:
    print("F")
else:
    print(f"{int(percentage)}%")