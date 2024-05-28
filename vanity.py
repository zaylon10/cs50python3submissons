def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # length check must be between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False
    # must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # no periods, spaces, or punctuation marks allowed
    if not s.isalnum():
        return False
    # numbers cannot be used in the middle; they must come at the end.
    num_found = False
    for char in s:
        if char.isdigit():
            if char == '0' and not num_found:
                return False  # first number can't be '0'
            num_found = True
        elif num_found:
            return False  # found a letter after a number

    return True

main()
