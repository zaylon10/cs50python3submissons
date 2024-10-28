import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    is_random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random = False
else:
    sys.exit(1)

figlet.getFonts()

if is_random == False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts)

msg = input("input : ")
print(f"Output:")
print(figlet.rendertext(msg))