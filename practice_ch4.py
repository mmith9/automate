def chapter4(a_list):
    if not a_list:
        return ""
    elif len(a_list)==1:
        return(str(a_list[0]))
    else:
        b_string=str(a_list[0])
        for item in a_list[1:-1]:
            b_string+=", "
            b_string+=str(item)
        b_string+=", and "
        b_string+=str(a_list[-1])

    return b_string

test1=[]
test2=[1]
test3=[1,2]
test4=[1,2,3]
test5=[1,2,3,4,]
print(test1, chapter4(test1))
print(test2, chapter4(test2))
print(test3, chapter4(test3))
print(test4, chapter4(test4))
print(test5, chapter4(test5))

