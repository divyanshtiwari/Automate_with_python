import pyperclip
# string in the book to copy 
'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''
text = pyperclip.paste()
# print(repr(text)) # using repr() built in function we can convert any string to a raw string, i.e. we can see what has been copied, including the escape sequence characters
# Note : I ended up having the program with a weird behaviour where only the last line was getting printed out. I thaught it to be a bug, as I thaught that my code is not concatinating the string and is just replacing the string and in the end the last string is getting replaces.
# eventually I got to know that my copied string is containg a escape sequence character \r which stands for carriage return. and this overwrites the currect line on the terminal
# the conclusion was, the code was working fine, and the string stored was also correct, the issue was that because of this \r character, on the terminal only the last line was getting showing as all the other lines we getting overwriten using direct print function.
textList = text.split('\r\n')
for i in range(len(textList)):
    textList[i] = ('* '+textList[i])
print('\n'.join(textList))
