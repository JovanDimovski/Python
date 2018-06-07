#!/usr/bin/env python
# coding: utf-8

import re
import time
import datetime
import sys
import os
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
    
def format_data(tm):
    result = []
    for i in range(0,len(tm[0])):
        for j in range(0,2):
            tm[j][i] = str(int(tm[j][i])+50)
        for j in range(2,4):
            if int(float(tm[2][i])) <10:
                tm[j][i]="0"+str(int(float(tm[j][i])))
            else:
                tm[j][i]=str(int(float(tm[j][i])))
    for data in tm:
        data = (''.join(data))
        data = re.findall('..............',data)
        result.append(data)
    return result

def process_data(r,tm):
    matches = re.findall('(?s)(<tr class="lo calendar-list-cl-tr.*?</tr>)', r, re.DOTALL)
    for match in range(0,len(matches)):
        m = re.search('(?s)<td style="font-weight:bold;.*?>(.*?)&#176;</td>', matches[match])
        tm[0].append(m.group(1))
        m = re.search('(?s)<td>(.*?)&#176;</td>', matches[match])
        tm[1].append(m.group(1))
        m = re.search('(?s)<td>(..?) mm</td>', matches[match])
        tm[2].append(m.group(1))
        m = re.search('(?s)<td>(..?(\.)?.?.?) CM</td>', matches[match])
        tm[3].append(m.group(1))
    return tm

def get_data(url):
    #if ose == 'win32':
    if ver == '2.6.2':
        response=urllib2.urlopen(url)
        r=response.read()
    else:
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        r=r.data.decode('utf-8')
    return r

def zooper(varname,varvalue):
    droid = android.Android()
    activity = 'org.zooper.zw.action.TASKERVAR'
    extras = {}
    extras['org.zooper.zw.tasker.var.extra.BUNDLE']={'org.zooper.zw.tasker.var.extra.STRING_VAR':varname,'org.zooper.zw.tasker.var.extra.STRING_TEXT':varvalue,'org.zooper.zw.tasker.var.extra.INT_VERSION_CODE':'1'}
    intent = droid.makeIntent(activity, None, None, extras, None, None, None).result
    droid.sendBroadcastIntent(intent)

def w_month():
    tm=[[None for i in range(0)] for j in range(4)]

    month=str(time.strftime("%B")).lower()
    url = 'http://www.accuweather.com/en/mk/skopje/227397/'+month+'-weather/227397?view=table'
    r = get_data(url)
    tm = process_data(r,tm)

    m = re.findall('(?s)href=\"(.*?>)', r,re.DOTALL)
    for match in range(0,len(m)):
        l = re.search('(?s)(.*?)(".*?next-month.*?)', str(m[match]))
        if len(str(l)) > 6:
            url=l.group(1)

    url=url.replace("&amp;", "&");
    r = get_data(url)
    tm = process_data(r,tm)
    for row in tm:
        print(row)
    MM = format_data(tm)
    for row in MM:
        for itm in row:
            print(itm)
        print("\n")
    #print (MM)

    if ose != 'win32':
        i=0
        j=0
        maxel=len(MM[i])
        while i<4:
            if i == 0:
                name="H"
            elif i == 1:
                name="L" 
            elif i == 2:
                name="R" 
            else:
                name="S"
            while j<maxel:
                k=j+1
                zooper('MF'+name+str(k),str(MM[i][j]))
                j+=1
            i+=1
            j=0
    return tm
w_month()
