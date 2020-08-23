x=input("Give ma an integer:")

x=int(x)

def collatz(x):
    if x % 2:
        return int(x*3+1)
    else:
        return int(x/2)

while x!=1:
    x=collatz(x)
    print(x)

