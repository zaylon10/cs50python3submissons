def main():
    word = input("")
    print(shorten(word))

def shorten(word):
    result = ""
    for character in word:
        if character in ('a','e','i','o','u'):
            continue
        else:
            result += character
    return result



if __name__ == "__main__":
    main()

