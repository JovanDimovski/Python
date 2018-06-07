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


def draw(in_arr,d,min_val,max_val,hilo,city,country,csch):
    dt = datetime.now()
    start_draw=(dt.minute*60+dt.second)*1000000+dt.microsecond
    ############################################
    range_val=int(max_val-min_val)
    r_r_val=255/range_val
    mm=int(max_val)-int(min_val)
    mm2=(255/mm)*0.999
    f_arr = []
    k=len(in_arr)
    
    
    hr=8
    vr=8
    """
    for i in range(0,len(in_arr)):
        for j in range(0,len(in_arr[0])):
            if in_arr[i][j] == None:
                in_arr[i][j]= 80
    n_in = numpy.asarray(in_arr,dtype=numpy.int16)
    
##############################################
    ndt = datetime.now()
    ndts=ndt.second*1000000+ndt.microsecond
    ############################################
    print("A: ",len(in_arr),"\t",len(in_arr[0]))
    print("N: ",len(in_arr),"\t",len(in_arr[0]))
    LEN=(70272*k)
    nc_arr = numpy.empty(LEN,dtype=numpy.uint8)
    #bc=0
    print("FULL LENGTH: ",LEN)
    for m in range(0,k):
        for n in range(0,366):
            #if n_in[m][n]!= None:
            pop=int(mm2*(-min_val+n_in[m][n]))
            for s in range(0,vr):
                row=(m*8+s)
                bc_r = (m*vr+s)*366*hr*3
            #print(row," : ",bc_r)
                for t in range(0,hr):
                    bc_c = bc_r + (n*hr+t)*3
                    #if  bc_r > 1740000 and bc_c > 1756000:
                     #   print(bc_c)
                    
                    if pop >=0 and pop < 256:
                        for p in (0,2):
                            bc_p=bc_c+p
                            nc_arr[bc_p]=pop
                        nc_arr[bc_c+0]=pop
                        nc_arr[bc_c+1]=pop
                        nc_arr[bc_c+2]=255
                            #if  bc_r > 1740000 and bc_c > 1756000:
                                #print("bc_c",bc_c)
                                #print("bc_p",bc_p)
                                
                    else:
                        for p in range(0,3):
                            bc_p=bc_c+p
                            nc_arr[bc_p]=0
                            #if  bc_r > 1740000 and bc_c > 1756000:
                                #print("bc_c",bc_c)
                                #print("bc_p",bc_p)
    ndt = datetime.now()
    ndtf=float(ndt.second*1000000+ndt.microsecond-ndts)/1000
    print("NUMPY: ",ndtf," miliseconds")
##            else:
##                for p in range(0,3):
##                    bc_p=bc_c+p
##                    nc_arr[bc_p]=0
                        #if  bc_r > 1740000 and bc_c > 1756000:
                            #print( "NONE")
                        
            #tmp = (m*8+s)*366*hr*3+(365*8+7)*3+2
            #print(row," : ",tmp)
    """
##############################################
    #print(bc_p)
    dt = datetime.now()
    start_for=(dt.minute*60+dt.second)*1000000+dt.microsecond
    ############################################
    for m in range(0,k):
        l_arr = []
        for n in range(0,366):
            arr = []
            #if m < k:
            if in_arr[m][int(n)]!= None:
                pop=mm2*(-float(min_val) + float(in_arr[m][int(n)]))
                if csch == 3:
                    if pop >=112 and pop < 256:
                        if pop >=223:
                            dpop = int(255-4*(pop-223))
                            #dpop = 255-int(pop-223)<<2
                            #print(dpop)
                            for s in range(0,hr):l_arr +=[0,0,dpop]
                        elif pop >= 144 and pop < 223:
                            #dpop=int(255-(2*(128/80)*(pop-144)))
                            dpop=int(255-3.2*(pop-144))
                            #print(dpop)
                            for s in range(0,hr):l_arr +=[0,dpop,255]
                        else:
                            red=int(8*(pop-112))
                            #red=int((pop-112))<<3
                            blue=255-red
                            #print(red," ",blue)
                            for s in range(0,hr):l_arr +=[blue,255,red]
                    elif  pop >=0 and pop < 112:
                        if pop >= 80:
                            dpop=128+int(2*(64/32)*(pop-80))
                            #dpop=128+int(pop-80)<<2
                            #print("pop: ",pop,"; 80-112",dpop)
                            for s in range(0,hr):l_arr +=[dpop,dpop,0]
                        elif pop >= 48 and pop < 80:
                            dpop=int(4*(pop-48))
                            #dpop=int((pop-48))<<2
                            #print(dpop)
                            for s in range(0,hr):l_arr +=[128+dpop,128-dpop,0]
                        elif pop >=16 and pop < 48:
                            dpop=int(4*(32-(32/48)*pop))
                            #dpop=int((32-(32/48)*pop))<<2
                            opop=128-dpop
                            ppop=128+dpop
                            #print(dpop," ",opop," ",ppop)
                            for s in range(0,hr):l_arr +=[ppop,opop,dpop]
                        else:
                            dpop=int(255-16*pop)
                            #dpop=255-int(pop)<<4
                            #print(dpop)
                            for s in range(0,hr):l_arr +=[192,dpop,96]
                    else:
                        for s in range(0,hr):l_arr +=[0,0,0]
                    """
                    if pop >=223 and pop < 256:
                        dpop = int(255-4*(pop-223))
                        for s in range(0,hr):l_arr +=[0,0,dpop]
                    elif pop >= 144 and pop < 223:
                        dpop=int(255-(2*(128/80)*(pop-144)))
                        for s in range(0,hr):l_arr +=[0,dpop,255]
                    elif pop >= 112 and pop < 144:
                        red=int(8*(pop-112))
                        green=255
                        blue=255-red
                        for s in range(0,hr):l_arr +=[blue,255,red]
                    elif pop >= 80 and pop < 112:
                        dpop=128+int(2*(64/32)*(pop-80))
                        for s in range(0,hr):l_arr +=[dpop,dpop,0]
                    elif pop >= 48 and pop < 80:
                        dpop=int(4*(pop-48))
                        for s in range(0,hr):l_arr +=[128+dpop,128-dpop,0]
                    elif pop >=16 and pop < 48:
                        dpop=int(4*(32-(32/48)*pop))
                        opop=128-dpop
                        ppop=128+dpop
                        for s in range(0,hr):l_arr +=[ppop,opop,dpop]
                    elif pop >=0 and pop < 16:
                        dpop=int(255-16*pop)
                        for s in range(0,hr):l_arr +=[192,dpop,96]
                    else:
                        for s in range(0,hr):l_arr +=[255,255,255]
                    """
                elif csch == 4:
                    if pop >= 0:
                        dpop=255-int(pop)
                        for s in range(0,hr):l_arr +=[255,dpop,dpop]


            else:
                for s in range(0,vr):l_arr +=[0,0,0]
        
        for g in range(0,8):
            f_arr += l_arr
    
    dt = datetime.now()
    end_for=(dt.minute*60+dt.second)*1000000+dt.microsecond
    ############################################

    LEN=(70272*(128-k))
    n_arr = numpy.zeros(LEN,dtype=numpy.uint8)
    
    if hilo == "hi":wfn="HIGH"
    elif hilo == "lo":wfn="LOW"
    elif hilo == "pr":wfn="PRECIPITATION"
    elif hilo == "cc":wfn="CLOUD COVER"

    directory = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+wfn+"/"
    filepath  = directory+str(country)+"_"+str(city)+".bmp"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    dt = datetime.now()
    start_write=(dt.minute*60+dt.second)*1000000+dt.microsecond
    f = open(filepath, 'wb')
    #f.write(bytes(new_get_header(2928,1024))+bytes(f_arr)+bytes(n_arr))
    f.write(bytes(new_get_header(2928,1024))+bytes(f_arr)+bytes(n_arr))
    f.close()

    dt = datetime.now()
    end_draw=(dt.minute*60+dt.second)*1000000+dt.microsecond
    ############################################
    #print("START TO FOR: ",str((start_for-start_draw)/1000)," miliseconds")
    #print("FOR         : ",str((end_for-start_for)/1000)," miliseconds")
    #print("FOR TO END  : ",str((end_draw-end_for)/1000)," miliseconds")
    #print("WRITE TO END: ",str((end_draw-start_write)/1000)," miliseconds")
    #print("START TO END: ",str((end_draw-start_draw)/1000)," miliseconds")
    
    return (end_draw-start_draw)/1000
