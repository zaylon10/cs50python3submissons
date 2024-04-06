# user input message
text = input("")
# split method called to seperate text
words =text.split(' ')
#Emoji dictionary created
emojis= {
    ":(":"🙁",
    ":)":"😊"
}
# output varaiable created
output =""
#for loop iterate through user choice of input
for word in words:
# converts compatible text into emoji from dictionary/ append message to output
    output += emojis.get(word, word) + " "
# print output
print(output)