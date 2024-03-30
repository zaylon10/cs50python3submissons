#prompt user for input
user = input()
#define function with parameter user.
def fillspace(user):
#split sentence into a a list of string.
    splitsen = user.split()
#join the list of strings together with '...'
    sentence = '...'.join(splitsen)
#print sentence
    print(sentence)
#call function with the input as the parameter.
fillspace(user)