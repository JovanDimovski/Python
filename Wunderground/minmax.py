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

def min_max3(in_arr,hilo):
    minv = 100000000
    maxv =-100000000
    std, avgv = stdev(in_arr)
    
    
    for i in range(0,len(in_arr)):
        for j in range(0,len(in_arr[0])):
            try:
                int(in_arr[i][j])
            except:
                exceptflag = True
            else:
                if int(in_arr[i][j]) > (avgv - 10*std) and int(in_arr[i][j]) < int(minv):
                    minv = in_arr[i][j]
                if int(in_arr[i][j]) < (avgv + 10*std) and int(in_arr[i][j]) > int(maxv):
                    maxv = in_arr[i][j]
    return minv, maxv

def min_max2(in_arr,hilo):
    std, avgv = stdev(in_arr)
    minv0 = 100000000
    minv1 = 100000000
    minv2 = 100000000
    maxv0 =-100000000
    maxv1 =-100000000
    maxv2 =-100000000
    maxv3 =-100000000
    maxv4 =-100000000
    maxv5 =-100000000
    maxv6 =-100000000
    maxv7 =-100000000
    maxv8 =-100000000
    maxv9 =-100000000
    avg = 0
    cnta = 0
    cntp = 0
    for i in range(0,len(in_arr)):
        for j in range(0,len(in_arr[0])):
            try:
                int(in_arr[i][j])
            except:
                exceptflag = True
            else:
                #if in_arr[i][j] < 1000*avg:
                cnta+=1
                if hilo is "pr":##ne znam dali raboti is kako ==
                    if in_arr[i][j] > 0:
                        cntp+=1
                if int(in_arr[i][j]) < int(minv0):
                    minv2 = minv1
                    minv1 = minv0
                    minv0 = in_arr[i][j]
                if int(in_arr[i][j]) > int(maxv0):
                    maxv9 = maxv8
                    maxv8 = maxv7
                    maxv7 = maxv6
                    maxv6 = maxv5
                    maxv5 = maxv4
                    maxv4 = maxv3
                    maxv3 = maxv2
                    maxv2 = maxv1
                    maxv1 = maxv0
                    maxv0 = in_arr[i][j]

    #print(str(minv2)+"\t"+str(maxv2)+"\t")
    #print(str(minv1)+"\t"+str(maxv1)+"\t")
    #print(str(minv0)+"\t"+str(maxv0)+"\t")
    #print(str(maxv0)+"\t"+str(maxv1)+"\t"+str(maxv2)+"\t"+str(maxv3)+"\t"+str(maxv4)+"\t"+str(maxv5)+"\t"+str(maxv6)+"\t"+str(maxv7)+"\t"+str(maxv8)+"\t"+str(maxv9)+"\t")
##    if (maxv0/maxv1) < (maxv1/maxv2)*3:
##        maxv = maxv0
##    else:
##        maxv = maxv1
    maxv = maxv0
    minv = minv0
    return minv, maxv

def stdev(in_arr):
    minv = 100000000
    maxv =-100000000
    avgv = 0
    cntv = 0
    sumv = 0
    std = 0
    for i in range(0,len(in_arr)):
        for j in range(0,len(in_arr[0])):
            try:
                int(in_arr[i][j])
            except:
                exceptflag = True
            else:
                #if int(in_arr[i][j]) > 0:
                sumv += in_arr[i][j]
                cntv += 1
    try:
        avgv=sumv/cntv
        difmeansum = 0
        for i in range(0,len(in_arr)):
            for j in range(0,len(in_arr[0])):
                try:
                    int(in_arr[i][j])
                except:
                    exceptflag = True
                else:
                    if int(in_arr[i][j]) > 0:
                        difmeansum += math.pow((in_arr[i][j]-avgv),2)
        std=math.sqrt((difmeansum/cntv))
##        print("\n\nSTDEV:\t "+str(std))
##        print("1SIG:\t"+str((avgv-std))+"\t"+str(avgv)+"\t"+str((avgv+std)))
##        print("2SIG:\t"+str((avgv-2*std))+"\t"+str(avgv)+"\t"+str((avgv+2*std)))
##        print("3SIG:\t"+str((avgv-3*std))+"\t"+str(avgv)+"\t"+str((avgv+3*std)))
##        print("5SIG:\t"+str((avgv-5*std))+"\t"+str(avgv)+"\t"+str((avgv+5*std)))
##        print("")
    except:
        print("STDEV_EXCEPTION")
    return std, avgv
            
