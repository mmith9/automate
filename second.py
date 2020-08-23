if None == print("bla"):

    print("aha!")

print(1,2,3,sep=";",end=".",flush=True)

glob_var=11

def testglob():
    global glob_var
    print(glob_var)
    glob_var="local"

testglob()
print(glob_var)

print(["xx"]+[123])

print(str.lower)

test=[1,2,
3,

4,5,
        3,      5,
                    3,
                    ]

print(test)

print(\
    1\
        ,3\
            )

def paramtest1(param):
    param=["param2"]

def paramtest2(param):
    param.remove("param1")
    param.append("param2")

param=["param1"]

print(param)
paramtest1(param)
print(param)
paramtest2(param)
print(param)

print([1,2,3,])

print(list(str(12341234)))
print(tuple([1,2,34,54,]))

list1=[1,2,3,4,[6,7]]
list2=list1
list1.append(5)
print(list2)

list3=[]
for x in list1:
    list3.append(x)
list2=list1[:]
list1.append(6)
print(id(list1),list1)
print(id(list2),list2)
print(id(list3),list3)

print([1,2,3,4][:2])
print([1,2,3,4][2:])

import pprint
message = 'It was a bright cold day in April, and the clocks were striking\
thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

spam={"black":"cat"}
if "cat" in spam.values():
    print("a")