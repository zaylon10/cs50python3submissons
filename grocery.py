def main():
    grocerylist = []
    while True:
        try:
            grocery = input()
            grocerylist.append(grocery.lower())  # Convert input to lowercase for case-insensitive comparison
            
        except EOFError:
            break

    grocerylist.sort()
    
    # Count occurrences of each item
    counts = {}
    for item in grocerylist:
        counts[item] = counts.get(item, 0) + 1

    # Print the grocery list with counts and in uppercase
    for item, count in sorted(counts.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
