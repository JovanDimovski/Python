#!/usr/bin/env python
# coding: utf-8

#import sys
#sys.path.append('/sdcard/com.googlecode.pythonforandroid/extras/python')

import re
import time
import datetime 
import sys
ose = sys.platform
ver = sys.version
if ose == 'win32':
    pass
else:
    import android
    
ver_s = re.split(' ',ver)
ver = ver_s[0]
if ver == '2.6.2':
    import urllib2

if re.compile('3.*').match(ver):
    import urllib3

    
def zooper(varname,varvalue):
    droid = android.Android()
    activity = 'org.zooper.zw.action.TASKERVAR'
    extras = {}
    extras['org.zooper.zw.tasker.var.extra.BUNDLE']={'org.zooper.zw.tasker.var.extra.STRING_VAR':varname,'org.zooper.zw.tasker.var.extra.STRING_TEXT':varvalue,'org.zooper.zw.tasker.var.extra.INT_VERSION_CODE':'1'}
    intent = droid.makeIntent(activity, None, None, extras, None, None, None).result
    droid.sendBroadcastIntent(intent)

def match_n(matches):
    for match in range(0,len(matches)):
        if int(matches[match]) <10:
            matches[match]="0"+matches[match]
        if int(matches[match]) == 100:
            matches[match]="99"
    return (''.join(matches))

print(ver+"\t"+ose)

def w_hours():
    millis = int(round(time.time() * 1000))

    dtime = int((int(round(time.time()))%86400)/3600)

    forc =[]
    temp =[]
    rain =[]
    snow =[]
    clou =[]
    now = datetime.datetime.time(datetime.datetime.now())
    for i in range(0,4):
        nowi=i*8+int(now.hour)
        #print(nowi)
        url='http://www.accuweather.com/en/mk/skopje/227397/hourly-weather-forecast/227397?hour='+str(nowi)
        
        response=urllib2.urlopen(url)
        rt=response.read()

        m = re.search('(?s)(<tr class="forecast".*?</tr>)', rt)

        line = m.group(1)
        matches = re.findall('(?s)h">(.*?)</div>', line, re.DOTALL)
        for match in range(0,len(matches)):
            matches[match] = re.sub(r"Partly Cloudy", "02", matches[match])
            matches[match] = re.sub(r"Mostly Cloudy|Cloudy", "00", matches[match])
            matches[match] = re.sub(r"Mostly Clear|Mostly Sunny", "05", matches[match])
            matches[match] = re.sub(r"Partly Sunny", "06", matches[match])
            matches[match] = re.sub(r"Clear|Sunny", "04", matches[match])
            matches[match] = re.sub(r"Showers", "03", matches[match])
            matches[match] = re.sub(r"Rain", "07", matches[match])
            matches[match] = re.sub(r"Snow|Flurries", "08", matches[match])
            matches[match] = re.sub(r"T-storms", "09", matches[match])
        mj = (''.join(matches))
        forc.append(mj)

        m = re.search('(?s)(<tr class="temp".*?</tr>)', rt)
        matches = re.findall('(?s)<td.*?>(.*?)&#176;</td>', m.group(1), re.DOTALL)
        for match in range(0,len(matches)):
            matches[match] = str(int(matches[match])+50)
        mj = (''.join(matches))
        temp.append(mj)

        m = re.search('(?s)(<tr class="rain ".*?</tr>)', rt)
        matches = re.findall('(?s)</div>(.*?)%</td>', m.group(1), re.DOTALL)
        rain.append(match_n(matches))

        m = re.search('(?s)(<tr class="snow ".*?</tr>)', rt)
        matches = re.findall('(?s)</div>(.*?)%</td>', m.group(1), re.DOTALL)
        snow.append(match_n(matches))

        m = re.search('(?s)Cloud Cover(.*?)</tr>', rt)
        matches = re.findall('(?s)<td.*?>(.*?)%</td>', m.group(1), re.DOTALL)
        clou.append(match_n(matches))

    MM = []
    MM.append(re.findall('............',''.join(forc)))
    MM.append(re.findall('............',''.join(temp)))
    MM.append(re.findall('............',''.join(rain)))
    MM.append(re.findall('............',''.join(snow)))
    MM.append(re.findall('............',''.join(clou)))

    i=0
    j=0
    while i<5:
        while j<5:
            print (MM[i][j])
            j+=1
        print ("\n")
        i+=1
        j=0

    if ose != 'win32':    
        i=0
        j=0
        while i<5:
            while j<5:
                zooper('PTW'+str(i)+str(j),str(MM[i][j]))
                j+=1
            i+=1
            j=0


    millis2 = int(round(time.time() * 1000))-millis
    print (millis2)

w_hours()
   
