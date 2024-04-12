# prompt user for input
user= input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
#define great answer function 
def greatanswer(x):
# use if else statements to gte desired output from user input
    if x == "42":
        print("yes")
    elif x == "forty two":
        print("yes")
    elif x == "forty-two":
        print("Yes")
    else:
        print("No")
#call function
greatanswer(user)