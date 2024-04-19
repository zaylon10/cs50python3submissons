#get user input
text = input("File name: ")
#convert input to lower with .lower string method
text1 = text.lower()
#create function that involves branching/ produces desired outcome w/ paramater
def mediatype(user):
    if ".jpeg" in user:
        print("image/jpeg")
    elif "jpg" in user:
        print("image/jpeg")
    elif ".png" in user:
        print("image/png")
    elif ".gif" in user:
        print("image/gif")
    elif ".pdf" in user:
        print("application/pdf")
    elif ".txt" in user:
        print("text/plain")
    elif ".zip" in user:
        print("application/zip")
    else:
        print("application/octet-stream")
#call function w/ arg
mediatype(text1)
