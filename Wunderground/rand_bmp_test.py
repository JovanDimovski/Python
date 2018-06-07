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

def new_bmp(xp,yp):
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


    body = []
    for i in range(0,yp):
        for j in range(0,xp):
            body+=[0,0,255]
        if xp %4 !=0:
            for k in range(0,4-(3*xp)%4):
                body+=[0]
                #print("kkk")

    f = open("C:/Python34/Scripts/Wunderground/headertest/"+str(xp)+"x"+str(yp)+"_calc.bmp", 'wb')
    f.write(bytes(header+body))
    f.close()
##    f = open("C:/Python34/Scripts/Wunderground/headertest/"+str(xp)+"x"+str(yp)+"_calc.bmp", 'ab')
##    f.write(bytes(body))
##    f.close()

for t in range(0,8):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond

    ############################################
    for i in range(26,38):
        for j in range(26,38):
            new_bmp(i,j)




    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print("DRAW TIME: ",fin," milliseconds")

for i in range(0,0):
    print("/././././.")









