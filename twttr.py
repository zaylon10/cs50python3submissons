word = input().lower()
def abbreviated(word):
    result = ""  # Initialize result variable
    for char in word:
        if char in ("a", "e", "i", "o", "u"):
            continue  # Skip vowels
        else:
            result += char  # Add non-vowel characters to result
    return result

abbrev = abbreviated(word)
print(abbrev)
