import re, pyperclip

# Indian phone number validator regularexpression
phoneRegex = re.compile(r'''(
(\+91|91)?       #Country code optional
([789]\d{3})    #service provider code
(\d{6})         # customer identification
)''',re.VERBOSE)

# email validator regularexpression
emailRegex = re.compile(r'''(
([a-z0-9.]+)    # userName
@               # atTheRate symbol
([a-z0-9.-]+)   # domain/subdomain name
(\.[a-z]{2,4})  # domain extension
)''',re.VERBOSE|re.IGNORECASE) # using re.IGNORECASE to check any capital letter with only the small once in the regex.

text = pyperclip.paste()
matches = []

for group in phoneRegex.findall(text):
    matches.append(group[0])

for group in emailRegex.findall(text):
    matches.append(group[0])

newText = '\n'.join(matches)
pyperclip.copy(newText)