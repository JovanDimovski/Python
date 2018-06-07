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

def draw(in_arr,d,mint,maxt,hilo,city,country,csch):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    mm=int(maxt)-int(mint)
    #print("Razlika max-min: "+str(mm))
    mm2=255/mm
    #print("Razlika max-min: "+str(mm)+"\t255/mm: "+str(mm2))
    f_arr = []
    #for x in range(0,16):
    #    arr.append(40)
    #    arr.append(50)
    #    arr.append(60)
    



    
    #f = open("C:/Users/Jovan/Desktop/1024b.bmp", 'r')
    f = open("C:/Python34/Scripts/WeatherData/IMG/2928x1024.bmp", 'r')
    cont6=f.read(54)
    f.close()
    temp = ':'.join(str(ord(x)) for x in cont6)
    #print(temp+"\n")
    result=cont6
    #l=int(1024/len(in_arr))
    #l=int(320/len(in_arr))
    #for m in range(0,1024):

    
    #for m in range(0,1024):
    for m in range(0,128):
        l_arr = []
        #if m%128==0:
            #print(m/128)

        #for n in range(0,2928):
        for n in range(0,366):
            arr = []
            #if n < 732:
            if n < 366:
                #k=int(m/8)
                k=m
                if k < len(in_arr):
                    #if in_arr[k][int((n/d)/8-0.1)]!= None:
                        #pop=float(0.999*mm2*(-float(mint) + float(in_arr[k][int((n/d)/8-0.1)])))
                    if in_arr[k][int((n/d)-0.1)]!= None:
                        pop=float(0.999*mm2*(-float(mint) + float(in_arr[k][int((n/d)-0.1)])))
                        if pop < 0 or pop > 255:
                            #print("::::::::::::::::::::::"+str(pop))
                            arr.append(0)
                            arr.append(255)
                            arr.append(0)
                        ##############RYWB#################
                        else:
                            if csch == 0:
                                if pop > 127:
                                    dpop=int(255-(2*(pop-128)))
                                    arr.append(0)
                                    arr.append(dpop)
                                    arr.append(255)
                                else:
                                    dpop=int(2*pop)
                                    arr.append(255)
                                    arr.append(dpop)
                                    arr.append(dpop)
                        ##############RYWB#################
                        ##############RYCB#################
                            elif csch == 1:
                                if pop >= 128:
                                    dpop=int(255-(2*(pop-128)))
                                    arr.append(0)
                                    arr.append(dpop)
                                    arr.append(255)
                                elif pop >= 64 and pop < 128:
                                    dpop=int(128+2*(pop-64))
                                    arr.append(dpop)
                                    arr.append(dpop)
                                    arr.append(0)
                                elif pop >= 0 and pop < 64:
                                    dpop=int(2*pop)
                                    arr.append(128+dpop)
                                    arr.append(128-dpop)
                                    arr.append(0)
                        ##############RYCB#################
                        #############RYWCB#################
                            elif csch == 2:
                                if pop >= 144:
                                    dpop=int(255-(2*(128/112)*(pop-144)))
                                    arr.append(0)
                                    arr.append(dpop)
                                    arr.append(255)
                                elif pop >= 112 and pop < 144:
                                    red=int(8*(pop-112))
                                    green=255
                                    blue=int(255-red)
                                    arr.append(blue)
                                    arr.append(255)
                                    arr.append(red)
                                elif pop >= 64 and pop < 112:
                                    dpop=int(128+2*(64/48)*(pop-64))
                                    arr.append(dpop)
                                    arr.append(dpop)
                                    arr.append(0)
                                elif pop >= 0 and pop < 64:
                                    dpop=int(2*pop)
                                    arr.append(128+dpop)
                                    arr.append(128-dpop)
                                    arr.append(0)
                        #############RYWCB#################
                        #############RYWCBP################
                            elif csch == 3:
                                if pop >=223:
                                    dpop = int(255-4*(pop-223))
                                    arr.append(0)
                                    arr.append(0)
                                    arr.append(dpop)
                                elif pop >= 144 and pop < 223:
                                    dpop=int(255-(2*(128/80)*(pop-144)))
                                    arr.append(0)
                                    arr.append(dpop)
                                    arr.append(255)
                                elif pop >= 112 and pop < 144:
                                    red=int(8*(pop-112))
                                    green=255
                                    blue=255-red
                                    arr.append(blue)
                                    arr.append(255)
                                    arr.append(red)
                                elif pop >= 80 and pop < 112:
                                    dpop=128+int(2*(64/32)*(pop-80))
                                    arr.append(dpop)
                                    arr.append(dpop)
                                    arr.append(0)
                                elif pop >= 48 and pop < 80:
                                    dpop=int(4*(pop-48))
                                    arr.append(128+dpop)
                                    arr.append(128-dpop)
                                    arr.append(0)
                                elif pop >=16 and pop < 48:
                                    dpop=int(4*(32-(32/48)*pop))
                                    opop=128-dpop
                                    ppop=128+dpop
                                    arr.append(ppop)
                                    arr.append(opop)
                                    arr.append(dpop)
                                elif pop < 16:
                                    dpop=int(255-16*pop)
                                    arr.append(192)
                                    arr.append(dpop)
                                    arr.append(96)
                            elif csch == 4:
                                if pop >= 0:
                                    dpop=255-int(pop)
                                    arr.append(255)
                                    arr.append(dpop)
                                    arr.append(dpop)
                    else:
                        arr+=[0,0,0]
                else:
                    arr+=[0,0,0]
            else:
                arr+=[255,255,255]
            for s in range(0,8):
                l_arr += arr
        for g in range(0,8):
            f_arr += l_arr
    barr = bytes (f_arr)
    #directory = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/IMG/"
    #filepath  = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/IMG/img"+hilo+"_"+city+"_"+str(chck)+".bmp"
    if hilo == "hi":
        wfn="HIGH"
    elif hilo == "lo":
        wfn="LOW"
    elif hilo == "pr":
        wfn="PRECIPITATION"
    elif hilo == "cc":
        wfn="CLOUD COVER"

    directory = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+wfn+"/"
    filepath  = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+wfn+"/"+str(country)+"_"+str(city)+".bmp"
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    #print(os.path.isfile(filepath))
    #if os.path.isfile(filepath):
        #GET_DATA_FROM_FILE#
    #    f = open(filepath, 'r')
    #    r = f.read()
    #    f.close()
    #f = open("C:/Python34/Scripts/WeatherData/IMG/bin_testweather_"+hilo+"_"+city+".bmp", 'w')
    f = open(filepath, 'w')
    f.write(cont6)
    f.close()
    #f = open("C:/Python34/Scripts/WeatherData/IMG/bin_testweather_"+hilo+"_"+city+".bmp", 'ab')
    f = open(filepath, 'ab')
    f.write(barr)
    f.close()
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print("DRAW TIME: ",fin," milliseconds")
    
