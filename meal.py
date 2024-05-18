#define function
def main():
    # Time input function
    time = input()
    #call function convert
    num = convert(time)
    print(num)
    #create branching for desired outcome
    if num >=7 and num <= 8:
        print("Breakfast Time")
    if num >= 12 and num <=13:
        print("Lunch Time")
    if num >= 18 and num <= 19:
        print("Dinner Time")
#define convert function
def convert(time):
    #use split function to make hours and minutes placeholder variables
    hours, minutes = time.split(":")
    #convert time
    new_min = float(minutes)/ 60
    return float(hours) + new_min    

#call function
if __name__ == "__main__":
    main()
    
