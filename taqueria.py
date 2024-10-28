#define dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# set total to 0
total_amount = 0
# implement indefinite loop until control-d is initiated.
while True:
    ''' try and except block implemented for error handling/control-d break from program/
     if statement to check if user input inside defined dictionary./menu selection to total ammount ''' 
    try:
       
        selection = input("Item: ").title()
        
        if selection in menu:
            total_amount += menu[selection]
            print("Total: $", end="")
            print(f"{total_amount:.2f}")
    
    except EOFError:
        print()
        break
