#! F:\My_Tech_Journey_2023\python\Automate_with_python\Scripts\python
# # The above first line is a shebang line which starts with a Hash and exclimation mark. This line define the location of the interpreter to be used for the execution of this program.
# Note1 : shebang line should be the first line in a script, otherwise it will not work as expected. 
# Note2 : defining a shebang with specific path will endup loosing potability for this shebang has provided virtual command, so that the portability can be retained.
# look at this page to find more : https://docs.python.org/3/using/windows.html#:~:text=4.8.2.-,Shebang%20Lines

# mclip.py - A multi-clipboard program.
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}

import sys
if(len(sys.argv) <2 ):
    print('Usage : python mclip.py [keyphrase] - copy phrase text')

keyphrase = sys.argv[1] # first command line arg is the keyphrase

import pyperclip
if keyphrase in TEXT.keys():
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+keyphrase+' copied to clipboard.')
else :
    print('There is no text for '+keyphrase)