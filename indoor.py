#This code solves the first cs50p assignment
#the task is to output any text that the user input as lowercase
#prompt user input
userinput =input()
# define a function for lowercase process/ parameter text(which will be the input from the user)
def lowercase(text):
#insert lowercase string method/ print statement
    print(text.lower())
#call function/ insert userinput as argument to be the value for the parameter described in function
lowercase(userinput)