import random
import sys

def parent(func_no):
    value1=random.randint(0,10)
    value2=func_no
    v3=[0]


    def child_one():
        vx=v3
        print(f"child one reporting,v1 is {value1} v2 is {value2}, v3 is {v3}")
        vx[0]+=1
        
    def child_two():
        print(f"child two reporting, v1 is {value1} v2 is {value2}, v3 is {v3}")
 
        
    if func_no==1:
        return [child_one,v3]
    else:
        return [child_two,v3]


first,v31=parent(1)
first()
print(id(v31))
second,v32=parent(2)
second()
print(id(v32))

v31[0]+=1
v32[0]+=1

print("again!")
first()
second()
second()
second()
second()

def func_w_value():
    v=[0]
    return v

vv=func_w_value()
vv[0]+=1
print(vv)

def f_get_f_count():
    uses=[0]
    bigvar=[0 for x in range(0,256**3*13)]
    def f_count():
        biglocal=bigvar
        ulocal=uses
        ulocal[0]+=1
        print(f"Function has been called {ulocal[0]} times!")
        print(sys.getrefcount(ulocal))
        print(sys.getsizeof(biglocal))
    print(psutil.virtual_memory())
   
    return f_count

import psutil
print(psutil.virtual_memory())

f_count=f_get_f_count()

print(psutil.virtual_memory())


f_count()
f_count()
f_count()
f_count()
f_count()

print(psutil.virtual_memory())
