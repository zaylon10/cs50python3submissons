from twttrtwo import shorten

def main():
    word=input("")
    processed_word(word)


def processed_word(word):
    result = shorten(word)
    print(result)

if __name__ == "__main__":
    main()