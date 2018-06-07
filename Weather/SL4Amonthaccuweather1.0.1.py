#!/usr/bin/env python
# coding: utf-8

import re
import time
import datetime
import os
import sys

ose = sys.platform

if ose != 'win32':
    import android
    import urllib2
else:
    import urllib3
millis = int(round(time.time() * 1000))

tmph =[]
tmpl =[]
rain =[]
snow =[]
month=str(time.strftime("%B")).lower()
url = 'http://www.accuweather.com/en/mk/skopje/227397/'+month+'-weather/227397?view=table'
    
if ose != 'win32':
    response=urllib2.urlopen(url)
    r=response.read()
else:
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    #print(r())
if ose != 'win32':  
    matches = re.findall('(?s)(<tr class="lo calendar-list-cl-tr.*?</tr>)', r, re.DOTALL)
else:
    matches = re.findall('(?s)(<tr class="lo calendar-list-cl-tr.*?</tr>)', r.data.decode('utf-8'), re.DOTALL)

for match in range(0,len(matches)):
    #print(">>>>>", matches[match])
    #print(match)
    m = re.search('(?s)<td style="font-weight:bold;.*?>(.*?)&#176;</td>', matches[match])
    tmph.append(m.group(1))
    #print("MAXT::::::::::::::::::::", m.group(1))
    m = re.search('(?s)<td>(.*?)&#176;</td>', matches[match])
    tmpl.append(m.group(1))
    #print("MINT::::::::::::::::::::", m.group(1))
    m = re.search('(?s)<td>(..?) mm</td>', matches[match])
    rain.append(m.group(1))
    #print("RAIN::::::::::::::::::::", m.group(1), "mm")
    m = re.search('(?s)<td>(..?(\.)?.?.?) CM</td>', matches[match])
    snow.append(m.group(1))
    #print("SNOW::::::::::::::::::::", round(float(m.group(1))), "CM")


m = re.findall('(?s)href=\"(.*?>)', rt,re.DOTALL)
for match in range(0,len(m)):
    #print(m[match])
    l = re.search('(?s)(.*?)(".*?next-month.*?)', str(m[match]))
    if len(str(l)) > 6:
        #print(m[match])
        #print(l.group(1))
        url=l.group(1)
#print(url)
url=url.replace("&amp;", "&");

#http = urllib3.PoolManager()
#r = http.request('GET', url)
#print (r.status, r.data)

if ose != 'win32':
    response=urllib2.urlopen(url)
    r=response.read()
else:
    http = urllib3.PoolManager()
    r = http.request('GET', url)

matches = re.findall('(?s)(<tr class="lo calendar-list-cl-tr.*?</tr>)', r, re.DOTALL)

for match in range(0,len(matches)):
    #print(">>>>>", matches[match])
    #print(match)
    m = re.search('(?s)<td style="font-weight:bold;.*?>(.*?)&#176;</td>', matches[match])
    tmph.append(m.group(1))
    #print("MAXT::::::::::::::::::::", m.group(1))
    m = re.search('(?s)<td>(.*?)&#176;</td>', matches[match])
    tmpl.append(m.group(1))
    #print("MINT::::::::::::::::::::", m.group(1))
    m = re.search('(?s)<td>(..?) mm</td>', matches[match])
    rain.append(m.group(1))
    #print("RAIN::::::::::::::::::::", m.group(1), "mm")
    m = re.search('(?s)<td>(..?(\.)?.?.?) CM</td>', matches[match])
    snow.append(m.group(1))
    #print("SNOW::::::::::::::::::::", round(float(m.group(1))), "CM")


#m = re.search('(?s)(<div class="calendar-controls".*?</div>)', r.data.decode('utf-8'))
#l = re.search('(?s)<a href="(.*?)"(.*?)</a>', m.group(1))
#m = re.findall('(?s)(<a(.*?)rt next-month(.*?)href="(.*?)">)', r.data.decode('utf-8'), re.DOTALL)
#print("\n",l.group(1))
    


"""
print(tmph)
print(tmpl)
print(rain)
print(snow)
"""
for match in range(0,len(tmph)):
    tmph[match] = str(int(tmph[match])+50)
mj1 = (''.join(tmph))
#print(mj1)


for match in range(0,len(tmpl)):
    tmpl[match] = str(int(tmpl[match])+50)
mj2 = (''.join(tmpl))
#print(mj2)

for match in range(0,len(rain)):
    if int(float(rain[match])) <10:
        rain[match]="0"+str(int(float(rain[match])))
    else:
        rain[match]=str(int(float(rain[match])))
mj3 = (''.join(rain))
#print(mj3)

for match in range(0,len(snow)):
    if int(float(snow[match])) <10:
        snow[match]="0"+str(int(float(snow[match])))
    else:
        snow[match]=str(int(float(snow[match])))
    
mj4 = (''.join(snow))
#print(mj4)


mj11=re.findall('..............',mj1)
mj21=re.findall('..............',mj2)
mj31=re.findall('..............',mj3)
mj41=re.findall('..............',mj4)
MM = []
MM.append(mj11)
MM.append(mj21)
MM.append(mj31)
MM.append(mj41)

print (MM)

if ose != 'win32':
    i=0
    j=0
    while i<4:
        while j<6:
            droid = android.Android()
            varname = 'PTWM'+str(i)+str(j)
            varvalue = str(MM[i][j])
            activity = 'org.zooper.zw.action.TASKERVAR'
            extras = {}
            extras['org.zooper.zw.tasker.var.extra.BUNDLE']={'org.zooper.zw.tasker.var.extra.STRING_VAR':varname,'org.zooper.zw.tasker.var.extra.STRING_TEXT':varvalue,'org.zooper.zw.tasker.var.extra.INT_VERSION_CODE':'1'}
            intent = droid.makeIntent(activity, None, None, extras, None, None, None).result
            droid.sendBroadcastIntent(intent)
            j+=1
        i+=1
        j=0



millis = int(round(time.time() * 1000))-millis
print(millis)


























