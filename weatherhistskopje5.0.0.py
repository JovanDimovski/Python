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
if ose == 'win32':
    import urllib3

def get_data(url,year,city,country):
    if ose == 'win32':
        directory = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/"
        filepath  = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/"+str(year)+".txt"
        if not os.path.exists(directory):
            os.makedirs(directory)
        #print(os.path.isfile(filepath))
        if os.path.isfile(filepath):
            #GET_DATA_FROM_FILE#
            f = open(filepath, 'r')
            r = f.read()
            f.close()
        else:
            #GET_DATA_FROM_WUNDERGROUND#
            http = urllib3.PoolManager()
            r = http.request('GET', url)
            r=r.data.decode('utf-8')
            #STORE_DATA_TO_FILE#
            f = open(filepath, 'w')
            f.write(r)
            f.close()   
    return r
#############################################
##def store_data(url,year,city):
##    if ose == 'win32':
##        filepath = "C:/Python34/Scripts/WeatherData/"+str(year)+".txt"
##        http = urllib3.PoolManager()
##        r = http.request('GET', url)
##        r = r.data.decode('utf-8')
##        f = open(filepath, 'w')
##        f.write(r)
##        #f = open(filepath, 'r')
##        #r = f.read()
##        f.close()
##    return r
#################################################
def process_data(url,year,city,country):
    file=get_data(url,year,city,country)
    line=file.split('<br />')
    table = []
    lastm = 0
    lastd = 0
    for n in range(1,len(line)-1):
        #print(line[n])
        temp=line[n].split(',')
        date=temp[0].split('-')
        date[0] = date[0][1:]
        pom=0
        if len(date) > 1:
            if int(date[1]) == 1:
                pom = 0
            elif int(date[1]) == 2:
                pom = 31
            elif int(date[1]) == 3:
                pom = 60
            elif int(date[1]) == 4:
                pom = 91
            elif int(date[1]) == 5:
                pom = 121
            elif int(date[1]) == 6:
                pom = 152
            elif int(date[1]) == 7:
                pom = 182
            elif int(date[1]) == 8:
                pom = 213
            elif int(date[1]) == 9:
                pom = 244
            elif int(date[1]) == 10:
                pom = 274
            elif int(date[1]) == 11:
                pom = 305
            elif int(date[1]) == 12:
                pom = 335
            if len(date) > 2:
                pom=pom+int(date[2])
            else:
                pom = -1
        else:
            pom = -2
        """
        if lastm != 0 and lastd != 0:
            if lastm == date[1]:
                if lastd == date[2]-1:

                else:
                    print("GAP")
            if lastm == date[1]-1:
                if date[2] == 1:

                else:
                    print("GAP")
        lastm = date[1]
        lastd = date[2]
        """
        row = []
        for val in date:
            row.append(val)
        for k in range(1,len(temp)):
            row.append(temp[k])
        row.append(str(pom))
        #print(row)
        table.append(row)
    #print(table)
    tmpstr=""
    for m in range(0,len(table)-1):
        for n in range(0,len(table[0])):
            tmpstr+=table[m][n]+"\t"
            #print(table[m][n]+"\t", end="")
        #print("")
        tmpstr+="\n"
    #print(tmpstr)
    return table
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
    print(str(maxv0)+"\t"+str(maxv1)+"\t"+str(maxv2)+"\t"+str(maxv3)+"\t"+str(maxv4)+"\t"+str(maxv5)+"\t"+str(maxv6)+"\t"+str(maxv7)+"\t"+str(maxv8)+"\t"+str(maxv9)+"\t")
    if (maxv0/maxv1) < (maxv1/maxv2)*3:
        maxv = maxv0
    else:
        maxv = maxv1
    minv=minv0
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
            
def draw(in_arr,d,mint,maxt,hilo,city,country,csch):
    mm=int(maxt)-int(mint)
    #print("Razlika max-min: "+str(mm))
    mm2=255/mm
    #print("Razlika max-min: "+str(mm)+"\t255/mm: "+str(mm2))
    arr = []
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
    for m in range(0,1024):
        #if m%128==0:
            #print(m/128)
        #for n in range(0,1024):
        for n in range(0,2928):
            #if n < 732:
            if n < 2928:
                k=int(m/8)
                if k < len(in_arr):
                    if in_arr[k][int((n/d)/8-0.1)]!= None:
                        pop=float(0.999*mm2*(-float(mint) + float(in_arr[k][int((n/d)/8-0.1)])))
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
                                    arr.append(255)
                                    arr.append(dpop)
                                    arr.append(255)
                            elif csch == 4:
                                if pop >= 0:
                                    dpop=255-int(pop)
                                    arr.append(255)
                                    arr.append(dpop)
                                    arr.append(dpop)
                    else:
                        arr.append(0)
                        arr.append(0)
                        arr.append(0)
                else:
                    arr.append(0)
                    arr.append(0)
                    arr.append(0)
            else:
                arr.append(255)
                arr.append(255)
                arr.append(255)

    barr = bytes (arr)
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
    filepath  = "C:/Python34/Scripts/WeatherData/ALL_IMG/"+wfn+"/"+str(country)+str(city)+".bmp"
    
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

def rm_img(city,country):    
    directory = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/IMG/"
    if  os.path.exists(directory):
        #os.rmdir(directory)
        shutil.rmtree(directory)
    
def get_cities(cc):
    filepath = "C:/Python34/Scripts/WeatherData/CountryCityCodes/codes.txt"
    #num_lines = sum(1 for line in open(filepath))
    #print(num_lines)
    cities=[]
    #all_cities=[]
    #print(cities)
    for line in open(filepath):
        city=line[0:29]
        city=city.rstrip()
        country=line[29:31]
        country=country.rstrip()
        urlc=line[33:37]
        urlc=urlc.rstrip()
        if country == cc:
            pom=[]
            pom.append(city)
            pom.append(urlc)
            #all_cities.append(pom)
            if len(urlc) > 0:
                cities.append(pom)
    #print(cities)
    #print(all_cities)
    return cities, cc

def get_rand_cities(num_c):
    rand_list = []
    filepath = "C:/Python34/Scripts/WeatherData/CountryCityCodes/codes.txt"
    num_lines = sum(1 for line in open(filepath))
    #for i in range(0,10*num_c):
    #    rand_list.append(random.randint(0, num_lines))
    #print(rand_list)
    cities=[]
    j=0
    while j < num_c:
        i=0
        line_n = random.randint(0, num_lines)
        #print(str(line_n))
        for line in open(filepath):
            if i == line_n:
                city=line[0:26]
                city=city.rstrip()
                country=line[29:31]
                country=country.rstrip()
                urlc=line[33:37]
                urlc=urlc.rstrip()
                pom=[]
                pom.append(city)
                pom.append(urlc)
                pom.append(country)
                if len(urlc) > 0:
                    cities.append(pom)
                    j+=1
            i+=1
    return cities

"""
cities = []
cities.append("BITOLA")
cities.append("SKOPJE")
cities.append("NEWYORK")
cities.append("ANCHORAGE")
cities.append("SIDNEY")
cities.append("BUFFALO")
cities.append("NAIROBI")
cities.append("SINGAPORE")
"""
countries = []
countries.append("MK")
#countries.append("YG")
#countries.append("CA")
ar = 1
if   ar == 0:
    print("Removing images, Please wait .. .  .   .    .     .")
    for cc in countries:
        cities, country = get_cities(cc)
        for city in cities:
            rm_img(city[0],country)
elif ar == 1:
    #for cc in countries:
        #cities, country = get_cities(cc)
    cities = get_rand_cities(20)
    for c in cities:
        print(c)    
    #print(cities)

    for city in cities:
        country = city[2]
        print(city[0])
        table = []
        flag = True
        count_to_flag = 0
        year=2015
        while flag:
            url="http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"

            temp = process_data(url,year,city[0],country)
            table.append(temp)
            #print(table[0][0])
            #print(len(temp))
            if len(temp) < 1:
                count_to_flag+=1
            else:
                count_to_flag = 0
            if  count_to_flag > 20:
                flag = False
            year-=1
        #print(table)

        ilo=[[None for j in range(0,367)] for k in range(0,len(table))]
        ihi=[[None for j in range(0,367)] for k in range(0,len(table))]
        ipr=[[None for j in range(0,367)] for k in range(0,len(table))]
        icc=[[None for j in range(0,367)] for k in range(0,len(table))]
        for l in range(0,len(table)):
            for m in range(0,len(table[l])):
                for n in range(0,len(table[l][m])):
                    if len(table[l][m][5]) >= 1:
                        ilo[l][int(table[l][m][len(table[l][m])-1])]=int(table[l][m][5])
                    if len(table[l][m][3]) >= 1:
                        ihi[l][int(table[l][m][len(table[l][m])-1])]=int(table[l][m][3])
                    if len(table[l][m][21]) >= 1:
                        #if float(table[l][m][21]) > 0.0:
                        #    print(table[l][m][21])
                        try:
                            pr=float(table[l][m][21])
                            #pr=math.sqrt(pr)
                            #pr=float(math.log2((pr*100+1))*14.5)
                            pr=float(math.log10((pr+1))*76.4)
                            ipr[l][int(table[l][m][len(table[l][m])-1])]=int(pr)
                        except:
                            #print(table[l][m][21])
                            excflg = True
                        #if ipr[l][int(table[l][m][len(table[l][m])-1])] > 0.0:
                            #print(ipr[l][int(table[l][m][len(table[l][m])-1])])
                    if len(table[l][m][22]) >= 1:
                        icc[l][int(table[l][m][len(table[l][m])-1])]=int(table[l][m][22])
        
        try:
            print("HIGH")
            hilo="hi"
            #mint, maxt = min_max3(ihi,hilo)
            mint=-25
            maxt= 55
            print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(3,4):
                draw(ihi,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        try:      
            print("LOW")
            hilo="lo"
            #mint, maxt = min_max3(ilo,hilo)
            mint=-40
            maxt= 40
            print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(3,4):
                draw(ilo,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        try:     
            print("PRECIPITATION")
            hilo="pr"
            mint, maxt = min_max2(ipr,hilo)
            #mint= 0
            #maxt= 150
            print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(3,4):
                draw(ipr,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        try:
            print("CLOUD COVER")
            hilo="cc"
            #mint, maxt = min_max3(icc,hilo)
            mint= 0
            maxt= 8
            print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(4,5):
                draw(icc,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        """
        #print(ihi)
        #print(ilo)

        tmpstr=""
        #print("TABLE: "+str(len(table)))
        for m in range(0,len(table)):
            #print("ROW"+str(m)+": "+str(len(table[m])))
            for n in range(0,len(table[m])):
                for k in range(0,len(table[m][n])):
                    if k < 6 or k == 21 or k == 22:
                        tmpstr+=table[m][n][k]+"\t"
                #print(table[m][n]+"\t", end="")
                tmpstr+=table[m][n][len(table[m][n])-1]
            #print("")
                tmpstr+="\n"
        print(tmpstr)
        """
