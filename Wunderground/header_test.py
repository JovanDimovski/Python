import os
import math
import shutil
import random
import sys
import urllib3
from datetime import datetime
import colorsys

import numpy
import math

def get_file_header(d1,d2):
    f = open("C:/Python34/Scripts/Wunderground/headertest/"+str(d1)+"x"+str(d2)+".bmp", 'r')
    header=f.read(54)
    #byte = 'a'
    byte_arr = []
    for i in range(0,len(header)):
        #print("Byte "+str(i+1)+": "+str(int('{0:08b}'.format(ord(header[i])),2)))
        byte_arr.append(int('{0:08b}'.format(ord(header[i])),2))
        #byte_arr.append('{0:08b}'.format(ord(header[i])))
    f.close()
    return byte_arr

def env(d1,d2):
    l=get_file_header(d1,d2)
    n=9
    for i in range(0, len(l), n):
        print(l[i:i+n])
    print("\n")

##for i in (1,2,4,255,256,1024):
##    print(str(i)+"x"+str(i)+".bmp")
##    env(i,i)
fhs = []
for i in (4,255,1024):
    fhs.append(get_file_header(i,i))
#print(fhs)
inda = []
for j in range(0,len(fhs[0])):    
    if int(fhs[0][j]) != int(fhs[1][j]) or int(fhs[0][j]) != int(fhs[2][j]):
       inda.append(j)
print(inda)

for j in range(0,len(fhs)):
    print(str(j)+": ",end="")
    sumb=int(fhs[j][34])+int(fhs[j][35])*256+int(fhs[j][36])*256*256
    dimb=int(fhs[j][18])+int(fhs[j][19])*256
    cbfd=math.ceil(dimb/4)*4*dimb*3
    bmps=int(fhs[j][2])+int(fhs[j][3])*256+int(fhs[j][4])*256*256
    for i in inda:
        print(str(fhs[j][i])+"\t",end="")

    print("\t bytes "+str(sumb)+"\t dimension "+str(dimb)+"\t calcB "+str(cbfd)+"\t BMPs "+str(bmps))

indb = []
for i in range(0,54):
    if not i in inda:
        indb.append(i)

print("")
for i in range(0,54):
    print(str(fhs[0][i])+" ",end="")
print("")

xp= 415
yp= 281
sb = math.ceil(xp/4)*4*yp*3
fsb= sb+54
header = []
sizebytes    = [fsb%256, int(fsb/256)%256, int(fsb/(256*256))%256, int(fsb/(256*256*256))%256]#mozi site nuli#sizebytes    = [0,0,0,0]
dimensionx   = [xp%256, int(xp/256)%256, int(xp/(256*256))%256, int(xp/(256*256*256))%256]
dimensiony   = [yp%256, int(yp/256)%256, int(yp/(256*256))%256, int(yp/(256*256*256))%256]
sizebytesbody= [sb%256, int(sb/256)%256, int(sb/(256*256))%256, int(sb/(256*256*256))%256]#mozi site nuli#sizebytesbody= [0,0,0,0]


header+=[66, 77]
header+=sizebytes
header+=[0, 0, 0, 0, 54, 0, 0, 0, 40, 0, 0, 0]
header+=dimensionx
header+=dimensiony
header+=[ 1, 0, 24, 0, 0, 0, 0, 0]
header+=sizebytesbody
header+=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(header)

print(get_file_header(xp,yp))



body = []
for i in range(0,yp):
    for j in range(0,xp):
        body+=[0,0,255]
    for k in range(0,4-(3*xp)%4):
        body+=[0]

f = open("C:/Python34/Scripts/Wunderground/headertest/"+str(xp)+"x"+str(yp)+"_calc.bmp", 'wb')
f.write(bytes(header))
f.close()
f = open("C:/Python34/Scripts/Wunderground/headertest/"+str(xp)+"x"+str(yp)+"_calc.bmp", 'ab')
f.write(bytes(body))
f.close()






