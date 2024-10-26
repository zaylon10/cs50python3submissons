# import module
import inflect
# create names list
names = []

# while loop until user inputs ctrl-d
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:

        print()
        break

output = p.join(names)
print("Adieu, audieu, to" + output)