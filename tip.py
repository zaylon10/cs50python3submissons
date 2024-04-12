#First code block was given by cs50p (partial code to be completed)
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
#define dollars to float function
def dollars_to_float(d):
# remove $ by using string method replace
    d1 = d.replace("$", "")
#return result
    return float(d1)

#define function percent to float
def percent_to_float(p):
#remove % by using replace
    p1 = p.replace("%", "")
#convert str input into float then divide by 100 to move decimal point to proper (tip) position.
    p2 = float(p1) / 100
#return result
    return (p2)

# call main function
main()
