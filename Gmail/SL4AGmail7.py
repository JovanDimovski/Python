#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import email
import re
import sys
import time
import base64
import urllib
import os

ose = sys.platform

if ose != 'win32':
    import android
    import urllib2
else:
    import requests

def date_time(dt3):
    day=0
    if   dt3[1]=="Mon,":day=1
    elif dt3[1]=="Tue,":day=2
    elif dt3[1]=="Wed,":day=3
    elif dt3[1]=="Thu,":day=4
    elif dt3[1]=="Fri,":day=5
    elif dt3[1]=="Sat,":day=6
    elif dt3[1]=="Sun,":day=7
    daym=dt3[2]
    month=0
    if   dt3[3]=="Jan":month="01"
    elif dt3[3]=="Feb":month="02"
    elif dt3[3]=="Mar":month="03"
    elif dt3[3]=="Apr":month="04"
    elif dt3[3]=="May":month="05"
    elif dt3[3]=="Jun":month="06"
    elif dt3[3]=="Jul":month="07"
    elif dt3[3]=="Aug":month="08"
    elif dt3[3]=="Sep":month="09"
    elif dt3[3]=="Oct":month="10"
    elif dt3[3]=="Nov":month="11"
    elif dt3[3]=="Dec":month="12"
    year=dt3[4]
    time=dt3[5].split(":")
    hour=time[0]
    minute=time[1]
    timestamp=str(year)
    timestamp+=str(month)
    if int(daym) < 10:
        timestamp+="0"
    timestamp+=str(daym)
    timestamp+=str(day)
    timestamp+=str(hour)
    timestamp+=str(minute)
    return timestamp

def b64_decode(su0):
    if re.match(r'^\s*$', su0)!=None:
        return "NOSUBJECT"
    parsed_string = su0.split("?")
    if len(parsed_string) > 1:
        if parsed_string[1] == 'UTF-8' and parsed_string[2] == 'Q' or parsed_string[2] == 'q' or parsed_string[2] == 'B':
            from email.header import decode_header
            decoded, enc = decode_header(su0)[0]
            su=decoded.decode(enc)
            return su
    return "NOTB64"

def subject_process(su0):
    su_b64=b64_decode(su0)
    if su_b64!="NOTB64":
        su=su_b64
    else:
        su=su0
    ins=u'\[ФИНКИ - WAN компјутерски мрежи 2013/2014\] - '
    ous=u'WAN '
    su4 =re.sub(re.compile(ins,re.MULTILINE|re.U), ous, su,0)
    ins=u'\[ФИНКИ - Информациони системи 2013/2014\] - '
    ous=u'Информациони системи '
    su4 =re.sub(re.compile(ins,re.MULTILINE|re.U), ous, su4,0)
    ins=u'\[ФИНКИ - Вештачка интелигенција 2013/2014\] - '
    ous=u'ФИНКИ ВИ '
    su4 =re.sub(re.compile(ins,re.MULTILINE|re.U), ous, su4,0)
    su=su4
    return su
def content_process(cn,sone,i,filei):
    if sone == 1:
        cn = re.sub(re.compile(r'(<head>(.*\n*)*?</head>)',re.MULTILINE), r'', cn,0)
        cn = re.sub(re.compile(r'^.*?(>ONE).*?$',re.MULTILINE), r'', cn,0)
        cn = re.sub(re.compile(r'(<a.*?</a>)',re.MULTILINE), r'', cn,0)
        cn = re.sub(re.compile(r'(<br>.*\n?)',re.MULTILINE), r'\n', cn,0)
        cn = re.sub(re.compile(r'(<.*?>)',re.MULTILINE), r'', cn,0)
        
    cn = re.sub(re.compile(r'<http://le.finki.ukim.mk>', re.MULTILINE), r'', cn,0)
    links = re.findall('(<[^@]*?>)', cn, re.MULTILINE | re.DOTALL)
    if ose!= 'win32':
        base="/storage/sdcard1/User/Gmail/Files/"
    else:
        base="C:/Python34/Scripts/Output/"
    path=base+str(i)+".pdf"
    if os.path.isfile(path):
        os.remove(path)
    for l in links:
        filei=filei+pow(2,i)
        l =re.sub(re.compile(r'(\r|\n)', re.MULTILINE), r'', l,0)
        if ose != 'win32':
            #ll=urllib.unquote(l)
            ll=l
        else:
            ll=urllib.parse.unquote(l)
        ll =re.sub(re.compile(r'<|>', re.MULTILINE | re.DOTALL), r'', ll,0)
        fn =re.sub(re.compile(r'http://(.*/)*', re.MULTILINE | re.DOTALL), r'', ll,0)
        fe =re.sub(re.compile(r'.*?\.', re.MULTILINE | re.DOTALL), r'', fn,0)
        path=base+str(i)+"."+fe
        if ose!= 'win32':
            #quote_ll = urllib.quote(ll)
            #response = urllib2.urlopen(quote_ll)
            response = urllib2.urlopen(ll)
            file_content = response.read()
        else:
            file_content=requests.get(ll).content
        f = open(path, 'wb')
        f.write(file_content)
        f.close()
        

    cn =re.sub(re.compile(r'^(>)>', re.MULTILINE), r'\1  ', cn,0)
    cn =re.sub(re.compile(r'^(>)( *?)>', re.MULTILINE), r'\1\2  ', cn,0)
    cn =re.sub(re.compile(r'^(>)', re.MULTILINE), r'  ', cn,0)
    cn =re.sub(re.compile(r'(-)-+', re.MULTILINE), r'\n\n', cn,0)
    cn =re.sub(re.compile(r'^( +)', re.MULTILINE), r'', cn,0)
    cn =re.sub(re.compile(r'^(_+)\s*', re.MULTILINE), r'', cn,0)
    #cn =re.sub(re.compile(r'((\n\s+)+\n)',re.MULTILINE), r'\n\n', cn,0)
    #cn =re.sub(re.compile(r'(\r\n\r\n)', re.MULTILINE), r'\n', cn,0)

    cn =re.sub(re.compile(r'(\n\s+\n\s+\n\s+\n)',re.MULTILINE), r'\n\n\n', cn,0)
    #cn =re.sub(re.compile(r'(\r\n\r\n)', re.MULTILINE), r'\n', cn,0)
    cn =re.sub(re.compile(r'(\r\n)', re.MULTILINE), r' ', cn,0)
        
    cn =re.sub(re.compile(r'<(.*?)>', re.MULTILINE | re.DOTALL), r'', cn,0)
    cn =re.sub(re.compile(r'http:(.*\r*\n*/)*?((.*\r*\n*)?)\.[a-z]\s*[a-z]\s*[a-z]\s*', re.MULTILINE | re.DOTALL), r' XXXXXXXXXXXXXXXXX ', cn,0)
    return cn, filei

def zooper_variable(name,value):
    if ose!= 'win32':
        droid = android. Android()
        varname = name
        varvalue = value
        activity = 'org.zooper.zw.action.TASKERVAR'
        extras = {}
        extras['org.zooper.zw.tasker.var.extra.BUNDLE']={'org.zooper.zw.tasker.var.extra.STRING_VAR':varname,'org.zooper.zw.tasker.var.extra.STRING_TEXT':varvalue,'org.zooper.zw.tasker.var.extra.INT_VERSION_CODE':'1'}
        intent = droid.makeIntent(activity, None, None, extras, None, None, None).result
        droid.sendBroadcastIntent(intent)
#####################################################################################################
#...............................^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^......................................#
#####################################################################################################

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login('username@gmail.com', 'password')
s,top =M.select("Primary")
temp=str(top[0]).split('\'',2)

if ose != 'win32':
    allmail=temp[0]
else:
    allmail=temp[1] 
filei=0
minm=0
i=minm
maxm=25
ml=[]
while i < maxm:
    mnum=str(int(allmail)-i)
    i+=1
    t, data = M.fetch(mnum, '(RFC822)')
    #ANDROID
    if ose != 'win32':
        msgd=str(data[0][1]).split('\r\n', 100 )
    #WINDOWS
    else:
        msgd=str(data[0][1]).split('\\r\\n', 100 )
    fr=" "
    su=" "
    dt=" "
    cn=" "
    sone=0

    #MESSAGE_FROM_STRING
    if ose!= 'win32':
        email_message_s = email.message_from_string(data[0][1])
    else:
        email_message_s = email.message_from_string(str(data[0][1].decode('utf-8')))
    #DATE
    dt=date_time((" "+email_message_s.get('Date')).split(" "))
    #FROM
    fr=email_message_s.get('From')
    fr =re.sub(re.compile(r'.*?<(.*?)>', re.MULTILINE), r'\1  ', fr,0)
    if fr.lstrip().rstrip() == "moj.one-noreply@one.mk":
        sone = 1
    #SUBJECT
    su0 = email_message_s.get('Subject')
    su = subject_process(su0)
    #CONTENT
    if   sone == 1: content_type="text/html"
    elif sone == 0: content_type="text/plain"
    for part in email_message_s.walk():
        if part.get_content_type() == content_type:
            
            content = part.get_payload(decode=True)
    cn = content.decode('utf-8')
    cn, filei = content_process(cn,sone,i,filei)
    #print(filei)    
    ml.append([fr,su,dt,cn])
    
outputstr = "&^%$#\n"
i=0
while i < (maxm-minm):
    j=0
    while j < 4:
        ml[i][j]=ml[i][j].lstrip().rstrip()
        ml[i][j]=ml[i][j].lstrip('"').rstrip('"')
        outputstr=outputstr+ml[i][j]+"&^%$#\n"
        name = 'MAIL'+str(i)+str(j)
        value = ml[i][j]
        zooper_variable(name,value)
        j+=1
    outputstr=outputstr+"\n=====================================================================\n"
    i+=1
i=0

zooper_variable("MAILFILES",str(filei))
print(str(filei))
print(outputstr)
M.close()
M.logout()
