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

import queue
import threading


import process_data
import minmax
import weather_codes
import draw
import new_draw
import new_draw_2
import get_data_multithread


def rm_img(city,country):    
    directory = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/IMG/"
    if  os.path.exists(directory):
        #os.rmdir(directory)
        shutil.rmtree(directory)

def draw_env(q,in_arr,d,min_val,max_val,hilo,city,country,c):
    #q.put(urllib3.PoolManager().request('GET', url).data.decode('utf-8'))
    q.put(new_draw_2.draw(in_arr,d,min_val,max_val,hilo,city,country,c))

cities = []
#cities.append("Bitola")
#cities.append("Skopje-Petrovec")
#cities.append("New York")
##cities.append("Anchorage")
##cities.append("Sidney")
cities.append("Buffalo")
##cities.append("Nairobi")
##cities.append("Singapore")
#cities.append("Seattle")

countries = []
##countries.append("GR")
countries.append("NO")
##countries.append("CA")
ar = 1
if   ar == 0:
    print("Removing images, Please wait .. .  .   .    .     .")
    for cc in countries:
        cities, country = weather_codes.get_cities(cc)
        for city in cities:
            rm_img(city[0],country)
elif ar == 1:
    c_c_r = 0
    if   c_c_r == 0:
        cities = weather_codes.get_cities(countries)
    elif c_c_r == 1:
        cities = weather_codes.get_cities(cities)
    elif c_c_r == 2:
        cities = weather_codes.get_cities(1)
    for c in cities:
        c[0] = c[0].replace('/',' ')
        print(c)
    #print(cities)
    get_data_multithread.fetch_data_multithread(cities,1900,2016)

    dt = datetime.now()
    start=(dt.minute*60+dt.second)*1000000+dt.microsecond
    ############################################
        
    for city in cities:
        country = city[2]
        print(city[0])
        table = []
        flag = True
        count_to_flag = 0
        year=2015
        while flag:
            url="http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"

            temp = process_data.process_data(url,year,city[0],country)
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
        #print("TABLE: ",len(table))

        ilo=[[None for j in range(0,367)] for k in range(0,len(table)-21)]
        ihi=[[None for j in range(0,367)] for k in range(0,len(table)-21)]
        ipr=[[None for j in range(0,367)] for k in range(0,len(table)-21)]
        icc=[[None for j in range(0,367)] for k in range(0,len(table)-21)]
        
        for l in range(0,len(table)):
            for m in range(0,len(table[l])):
                #for n in range(0,len(table[l][m])):
                dy = int(table[l][m][len(table[l][m])-1])
                if len(table[l][m][5]) >= 1: ilo[l][dy]=int(table[l][m][5])
                if len(table[l][m][3]) >= 1: ihi[l][dy]=int(table[l][m][3])
                if len(table[l][m][21]) >= 1:
                    try:
                        pr=float(table[l][m][21])
                        pr=float(math.log10((pr+1))*76.4)
                        ipr[l][dy]=int(pr)
                    except:
                        excflg = True
                if len(table[l][m][22]) >= 1: icc[l][dy]=int(table[l][m][22])
        

        
        ############################################
        qlen=3
        q = queue.Queue()
        ##
        t = threading.Thread(target=draw_env, args = (q,ihi,1,-25,55,"hi",city[0],country,3))
        t.daemon = True
        t.start()
        ##
        t = threading.Thread(target=draw_env, args = (q,ilo,1,-40,40,"lo",city[0],country,3))
        t.daemon = True
        t.start()
        ##
        min_val, max_val = minmax.min_max2(ipr,"pr")
        if min_val != max_val:
            t = threading.Thread(target=draw_env, args = (q,ipr,1,min_val,max_val,"pr",city[0],country,3))
            t.daemon = True
            t.start()
            qlen+=1
        ##
        t = threading.Thread(target=draw_env, args = (q,icc,1,0,8,"cc",city[0],country,4))
        t.daemon = True
        t.start()
        ##
        
        ############################################
        """
        for arr in (ilo,ihi,ipr,icc):
            lh =len(arr)
            print("iloihi",lh)
            lh-=1
            while lh >= 0:
                empty_in_row=0
                for j in range(0,len(arr[0])):
                    if arr[lh][j] == None:
                        empty_in_row+=1
                if empty_in_row == 367:
                    arr.pop(lh)
                else:
                    break
                lh-=1
            lh =len(arr)
            print(lh)
        #for arr in (ilo,ihi,ipr,icc):
            #print(len(arr))
        """
        """
        new_draw_2.draw(ihi,1,-25,55,"hi",city[0],country,3)
        new_draw_2.draw(ilo,1,-40,40,"lo",city[0],country,3)
        min_val, max_val = minmax.min_max2(ipr,"pr")
        if min_val != max_val:
            new_draw_2.draw(ipr,1,min_val,max_val,"pr",city[0],country,3)
        new_draw_2.draw(icc,1,0,8,"cc",city[0],country,4)
        """
        ###########################################
        for i in range(0,qlen):
            s = q.get()
            #print(i,". ",s)
        ############################################
         
        ############################################

    dt = datetime.now()
    fin=float((dt.minute*60+dt.second)*1000000+dt.microsecond-start)/1000
    print("All : ",fin," milliseconds")


    """
        #except:
        #    except_flag = True
        #    print("DRAW ERR")
        try:      
            #print("LOW")
            hilo="lo"
            #mint, maxt = minmax.min_max3(ilo,hilo)
            mint=-40
            maxt= 40
            #print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(3,4):
                new_draw.draw(ilo,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        try:     
            #print("PRECIPITATION")
            hilo="pr"
            
            #mint= 0
            #maxt= 150
            #print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(3,4):
                new_draw.draw(ipr,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
        try:
            #print("CLOUD COVER")
            hilo="cc"
            #mint, maxt = minmax.min_max3(icc,hilo)
            mint= 0
            maxt= 8
            #print("MIN:\t"+str(mint)+"MAX:\t"+str(maxt))
            for chck in range(4,5):
                new_draw.draw(icc,1,mint,maxt,hilo,city[0],country,chck)
        except:
            except_flag = True
            print("DRAW ERR")
    """
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
