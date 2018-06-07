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
import time
from datetime import datetime

def get_cities_by_f(in_arr,f):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    filepath = "C:/Python34/Scripts/WeatherData/CountryCityCodes/codes.txt"
    cities=[]
    for line in open(filepath):
        city=line[0:26]
        city=city.rstrip()
        country=line[29:31]
        country=country.rstrip()
        urlc=line[33:37]
        urlc=urlc.rstrip()
        if f:
            pf=country
        else:
            pf=city
        if pf in in_arr:
            pom=[]
            pom.append(city)
            pom.append(urlc)
            pom.append(country)
            if len(urlc) > 0:
                cities.append(pom)
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print(fin)
    return cities

def get_rand_cities(num_c):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
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
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print(fin)
    return cities

def get_cities(in_var):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    cities = []
    if isinstance(in_var, int):
        cities = get_rand_cities(in_var)
    elif isinstance(in_var, list):
        is_country= True
        for element in in_var:
            #print(element)
            if len(element) > 2:
                is_country = False
                #print(is_country)
        cities = get_cities_by_f(in_var,is_country)
    else:
        cities.append(["ERROR","NOT LIST OR INT","???"])
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print("ENV: ",fin)
    return cities

"""    
cities = []
cities.append("Bitola")
cities.append("Skopje-Petrovec")
cities.append("New York")
cities.append("Anchorage")
cities.append("Sidney")
cities.append("Buffalo")
cities.append("Nairoby")
cities.append("Singapore")
countries = []
countries.append("MK")
countries.append("YG")
countries.append("BU")

print("BY CITY: ")
for city in get_cities(cities):
    print(city)
print("RANDOM: ")
for city in get_cities(8):
    print(city)
print("BY COUNTRY: ")
for city in get_cities(countries):
    print(city)
for city in get_cities("pp"):
    print(city)
"""

