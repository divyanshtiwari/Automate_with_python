import pprint
message = 'This is the best day of my life, as I am learning alot of python concepts by reading for books and writing code'
count = {}
for ch in message:
    count.setdefault(ch,0)
    count[ch] += 1

print(count)
pprint.pprint(count)