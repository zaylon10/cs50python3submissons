# variables x y and z prompting user for input
x= int(input())
y = input("")
z = int(input())

# create function with branching to achieve desired outcome/ parameter y as placeholder
def result(y):
    if y == "+":
        answer = x + z
    if y == "/":
        answer = x / z
    if y == "%":
        answer = x % z
    if y == "*":
        answer = x * z
    if y == "-":
        answer = x - z
#print a float from branching results
    print(float(answer))
    
#call function with arg
result(y)