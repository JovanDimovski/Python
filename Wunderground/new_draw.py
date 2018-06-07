#http://www.wunderground.com/history/airport/LWSK/1999/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=1999&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&MR=1&format=1
#!/usr/bin/env python
# coding: utf-8

import re
import time
import datetime
import sys
import os
import math
import shutil
import random
ose = sys.platform
import urllib3
from datetime import datetime
import colorsys

import numpy
import math

def new_get_header(xp,yp):
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
    return header

"""
    body = []
    for i in range(0,yp):
        for j in range(0,xp):
            body+=[0,0,255]
        if xp %4 !=0:
            for k in range(0,4-(3*xp)%4):
                body+=[0]
                #print("kkk")
"""

def get_file_header():
##    dt = datetime.now()
##    start=dt.second*1000000+dt.microsecond
##    
##    ############################################
    f = open("C:/Python34/Scripts/WeatherData/IMG/2928x1024.bmp", 'r')
    header=f.read(54)
    f.close()
##    ############################################
##    dt2 = datetime.now()
##    print(dt)
##    print(dt2)
##    fin=float(dt2.second*1000000+dt2.microsecond-start)
##    #print("FETCH HEADER: ",fin," micros")
    return header

def draw(in_arr,d,min_val,max_val,hilo,city,country,csch):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    range_val=int(max_val-min_val)
    r_r_val=255/range_val
    mm=int(max_val)-int(min_val)
    mm2=255/mm
    f_arr = []
    #temp = ':'.join(str(ord(x)) for x in cont6)
    #header=get_file_header()
    k=len(in_arr)
    ##################NUMPY#####################
    #LENA=(70272*k)
    #LEN =(1098*k)
    #n_carr = numpy.zeros(LEN,dtype=numpy.uint8)
    #n_farr = numpy.zeros(LENA,dtype=numpy.uint8)
    #in_arr_cnt=0
    #print(LEN)
###############################################################################
    """
    in_arr_cnt=0
    for m in range(0,k):
        #for s in range(0,8):
        #l_arr = []
        for n in range(0,366):
        #for t in range(0,8):
            #arr = []
            #if in_arr_cnt%100000 == 0:
            #    print(in_arr_cnt)
            if in_arr[m][int(n)]!= None:
                pop=int(float(0.999*mm2*(-float(min_val) + float(in_arr[m][int(n)]))))
            
                #dodeli prva vrednost
                #
                n_carr[in_arr_cnt]=pop
                in_arr_cnt+=1
                #dodeli vtora
                #
                n_carr[in_arr_cnt]=pop
                in_arr_cnt+=1
                #dodeli treta
                #
                n_carr[in_arr_cnt]=255
                in_arr_cnt+=1
                #print("::",pop)
            else:
                #dodeli prva vrednost
                #
                n_carr[in_arr_cnt]=0
                in_arr_cnt+=1
                #dodeli vtora
                #
                n_carr[in_arr_cnt]=0
                in_arr_cnt+=1
                #dodeli treta
                #
                n_carr[in_arr_cnt]=0
                in_arr_cnt+=1
                #arr+=[0,0,0]
    for i in range(0,LEN):
        for j in range(0,8):
            ij=j*366*8+i*8
            #print(n_carr[i],"i=",i)
            n_farr[ij]    =n_carr[i]
            n_farr[ij+1]  =n_carr[i]
            n_farr[ij+2]  =n_carr[i]
            n_farr[ij+3]  =n_carr[i]
            n_farr[ij+4]  =n_carr[i]
            n_farr[ij+5]  =n_carr[i]
            n_farr[ij+6]  =n_carr[i]
            n_farr[ij+7]  =n_carr[i]
    """
    ofc = datetime.now()
    ofc_s=ofc.second*1000000+ofc.microsecond
##        ############################################
    hr=8
    vr=8
    for m in range(0,k):
        l_arr = []
        for n in range(0,366):
            arr = []
            #if m < k:
            if in_arr[m][int(n)]!= None:

                pop=float(0.999*mm2*(-float(min_val) + float(in_arr[m][int(n)])))
                if csch == 3:
                    if pop < 0 or pop > 255:
                        for s in range(0,hr):l_arr +=[255,255,255]
                    elif pop >=223:
                        dpop = int(255-4*(pop-223))
                        for s in range(0,hr):l_arr +=[0,0,dpop]
##                        arr.append(0)
##                        arr.append(0)
##                        arr.append(dpop)
                    elif pop >= 144 and pop < 223:
                        dpop=int(255-(2*(128/80)*(pop-144)))
                        for s in range(0,hr):l_arr +=[0,dpop,255]
##                        arr.append(0)
##                        arr.append(dpop)
##                        arr.append(255)
                    elif pop >= 112 and pop < 144:
                        red=int(8*(pop-112))
                        green=255
                        blue=255-red
                        for s in range(0,hr):l_arr +=[blue,255,red]
##                        arr.append(blue)
##                        arr.append(255)
##                        arr.append(red)
                    elif pop >= 80 and pop < 112:
                        dpop=128+int(2*(64/32)*(pop-80))
                        for s in range(0,hr):l_arr +=[dpop,dpop,0]
##                        arr.append(dpop)
##                        arr.append(dpop)
##                        arr.append(0)
                    elif pop >= 48 and pop < 80:
                        dpop=int(4*(pop-48))
                        for s in range(0,hr):l_arr +=[128+dpop,128-dpop,0]
##                        arr.append(128+dpop)
##                        arr.append(128-dpop)
##                        arr.append(0)
                    elif pop >=16 and pop < 48:
                        dpop=int(4*(32-(32/48)*pop))
                        opop=128-dpop
                        ppop=128+dpop
                        for s in range(0,hr):l_arr +=[ppop,opop,dpop]
##                        arr.append(ppop)
##                        arr.append(opop)
##                        arr.append(dpop)
                    elif pop < 16:
                        dpop=int(255-16*pop)
                        for s in range(0,hr):l_arr +=[192,dpop,96]
##                        arr.append(192)
##                        arr.append(dpop)
##                        arr.append(96)
                elif csch == 4:
                    if pop >= 0:
                        dpop=255-int(pop)
                        for s in range(0,hr):l_arr +=[255,dpop,dpop]
##                        arr.append(255)
##                        arr.append(dpop)
##                        arr.append(dpop)

            else:
                for s in range(0,vr):l_arr +=[0,0,0]
        
            #else:
            #    arr+=[0,0,0]
            #for s in range(0,8):
            #    l_arr += arr
            
        for g in range(0,8):
            f_arr += l_arr
    
        ############################################
    ofc = datetime.now()
    ofc_f=float(ofc.second*1000000+ofc.microsecond-ofc_s)/1000
    print("For: ",ofc_f," miliseconds")

        
###############################################################################
##    ofc = datetime.now()
##    ofc_s=ofc.second*1000000+ofc.microsecond
##    ############################################
##    
    #arr=[0 for aaa in range(0,(70272*(128-k)))]

    #f_arr += arr
    ##################NUMPY#####################
    LEN=(70272*(128-k))
    n_arr = numpy.zeros(LEN,dtype=numpy.uint8)
##    b_n_arr=bytes (n_arr)
##    ############################################
##    ofc = datetime.now()
##    ofc_f=float(ofc.second*1000000+ofc.microsecond-ofc_s)/1000
##    #print("Fill in black ",ofc_f," milliseconds")
##    
##    #for m in range(k,128):
##    #    arr=[0 for aaa in range(0,70272)]
##    #    f_arr += arr
##            
##    barr = bytes (f_arr)
    #barr = bytes(n_carr)
    #barr = bytes(n_farr)
##    barr+= b_n_arr
    if hilo == "hi":
        wfn="HIGH"
    elif hilo == "lo":
        wfn="LOW"
    elif hilo == "pr":
        wfn="PRECIPITATION"
    elif hilo == "cc":
        wfn="CLOUD COVER"

    directory = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+wfn+"/"
    filepath  = directory+str(country)+"_"+str(city)+".bmp"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
##    dt2 = datetime.now()
##    start2=dt2.second*1000000+dt2.microsecond
##    ############################################
    f = open(filepath, 'wb')
    f.write(bytes(new_get_header(2928,1024))+bytes(f_arr)+bytes(n_arr))
    f.close()
    """
    f = open(filepath, 'w')
    f.write(get_file_header())
    f.close()
    """
##    ############################################
##    dt2 = datetime.now()
##    fin2=float(dt2.second*1000000+dt2.microsecond-start2)/1000
##    #print("HEAD WRITE: ",fin2," milliseconds")
##    dt3 = datetime.now()
##    start3=dt3.second*1000000+dt3.microsecond
##    ############################################
    """
    f = open(filepath, 'ab')
    f.write(barr)
    f.close()
    """
##    ############################################
##    dt3 = datetime.now()
##    fin3=float(dt3.second*1000000+dt3.microsecond-start3)/1000
##    #print("CONT WRITE: ",fin3," milliseconds")
##    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print("DRAW TIME: ",fin," milliseconds")
    
