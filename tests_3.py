from pathlib import Path
import os
import shelve
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug("program start")

a=Path('bla','ble','blah')
print(a)
print(str(a))
#print(len(a))
print(len(str(a)))

a=a / 'test'

print(a)
print(type(a))

print(Path.cwd())
print(Path.home())
print(os.listdir())
#os.makedirs('testdir')

print(os.path.abspath('.'))
print(os.path.relpath('c:\\'))
apath=Path('collatz.py')
aabspath=os.path.abspath(apath)
aabspath=Path(aabspath)
print(type(aabspath))
print(aabspath.drive)
print(aabspath.parent)
print(aabspath.stem)
print(aabspath.name)
print(aabspath.suffix)

alist=[1,2,3,4,5,6,7,8,9,10]
atuple=(1,2,3,4,5,6,7,8,9,0)
adir={1:1,2:2,3:3,4:4,5:5}

logging.debug("shelving a file")

sfile=shelve.open("shelvefile")
sfile["alist"]=alist
sfile["adir"]=adir

sfile.close()

alist=[]
adir={}

logging.debug("deshelving")
sfile=shelve.open("shelvefile")
print(sfile["alist"])
print(sfile["adir"])

blist=sfile["alist"]
bdir=sfile["adir"]


print(list(sfile.keys()))
print(list(sfile.values()))

print(blist)
print(bdir)

logging.debug("pretty printing file")
import pprint
afile=open("afile.py","w")
astring=pprint.pformat(blist)
afile.write("alist=" + astring + "\n")

import shutil

#for a, b, c in os.walk("c:\\temp\\"):
#    print(a,b,c)

logging.debug("zipping a file")
import zipfile

zfile=zipfile.ZipFile("newzip.zip","w")
zfile.write("tests_1.py",compress_type=zipfile.ZIP_LZMA)
zfile.close()


logging.debug("file zipped")





logging.debug("end of program reached")