#prompt user for input
user=input("Greeting: ")
#define function bank
def bank(x):
#use captitalization string method/use branching/nested to get desired output from users input
    greeting = x.capitalize()
    if greeting[0] == "H":
        if greeting[:5] == "Hello":
            print("$0")
        else:
            print("$20")
    else:
        print("$100")
#call function
bank(user)