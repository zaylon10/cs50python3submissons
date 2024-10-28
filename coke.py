change = int(input("Enter the amount of change in cents: "))
# Define a function that produces the desired output by employing logical branching. 
def buy_a_Coke(change):
    if change % 5 == 0:
        if change > 50:
            amount = change - 50
        else:
            amount = 0
    else:
        amount = change
    return amount

amount = buy_a_Coke(change)
receipt = "Change Amount: " + str(amount) + " cents"
print(receipt)
