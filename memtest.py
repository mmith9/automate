import sys
import psutil
import random

sl = []
i = 0
# some magic 1024 - overhead of string object
fill_size = 1024
#if sys.version.startswith('2.7'):
#    fill_size = 1003
#if sys.version.startswith('3'):
#    fill_size = 497
print(fill_size)
MiB = 0
s=""
for j in range(0,1024):
    s+=str(random.randint(0,9))

rndfile=open("rndfile.txt","w")
while True:
    s=""
    for j in range(0,1024):
        s+=str(random.randint(0,9))
    rndfile.write(s)

    try :
        sl.append(s)
    except:
        print(f"failure to append at {sys.getsizeof(sl)}")
        sys.exit()

    if i == 0:
        try:
            sys.stderr.write('size of one string %d\n' % (sys.getsizeof(s)))
        except AttributeError:
            pass
    i += 1
    if i % 1024 == 0:
        MiB += 1
        if MiB % 25 == 0:
            sys.stderr.write('%d [MiB]\n' % (MiB))
            print(psutil.virtual_memory())
            print(sys.getsizeof(sl))
            print(f"{i} [KiB]")
            #s=""
            #for i in range(0,1024):
            #    s+=str(random.randint(0,9))
            #print(s)


