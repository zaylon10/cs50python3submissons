#user input
user = input()
#Define a function to iterate through the input, checking for uppercase letters and replacing them with underscores.
def modified_word(user):
    snake_case= ""
    for char in user:
        if char.isupper():
            snake_case += "_" + char 
        else :
            snake_case += char
    return snake_case
#Variable to hold the place of the defined function.
sc = modified_word(user)
print(sc)