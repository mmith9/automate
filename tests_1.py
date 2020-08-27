import sys,pyperclip

"""this is a 
    multiline
        comment
ends
here"""


print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')


print("".join(["1","2","3","4"]))
print("An example of splitting".split())
print("A partitioning test".partition("part"))
a, b, c = [1,2,3]
print("abs".center(10,"*"),a,b,c)

print(ord("Ź"))
print(chr(322))

pyperclip.copy("Hello world!")
pyperclip.paste()

if len(sys.argv) < 2:
    print("usage test.py phrase")
else:
    print(sys.argv[0])
    print(sys.argv[1])

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""}

if sys.argv[1] in TEXT:
    pyperclip.copy(TEXT[sys.argv[1]])
    print("text"+pyperclip.paste()+" copied")
else:
    print("no "+sys.argv[1]+" in texts")

