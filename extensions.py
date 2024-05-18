# user input
user = input("")
#create function that involves branching to get desired output
def mediatype(user):
    user = user.lower().strip()
    if user.endswith(".gif"):
        return print("image/gif")
    elif user.endswith(".jpeg"):
        return print("image/jpeg")
    elif user.endswith(".jpg"):
        return print("image/jpeg")
    elif user.endswith(".png"):
        return print("image/png")
    elif user.endswith(".pdf"):
        return print("application/pdf")
    elif user.endswith(".txt"):
        return print("text/plain")
    elif user.endswith(".zip"):
        return print("application/zip")
    else:
        print("application/octec-stream")
# call function with input variable as arg
mediatype(user)