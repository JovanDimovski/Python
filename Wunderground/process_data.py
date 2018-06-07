import os
import urllib3
from datetime import datetime

import queue
import threading

def get_data(url,year,city,country):
    #if ose == 'win32':
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

def get_data_from_file(url,year,city,country):
    directory = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/"
    filepath  = "C:/Python34/Scripts/WeatherData/"+str(country)+"/"+str(city)+"/"+str(year)+".txt"
    if not os.path.exists(directory):
        print("No directory named "+directory)
    if os.path.isfile(filepath):
        f = open(filepath, 'r')
        r = f.read()
        f.close()
    else:
        print("No file named "+filepath)
    return r

def process_data(url,year,city,country):
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    #file=get_data(url,year,city,country)
    file=get_data_from_file(url,year,city,country)
    dt = datetime.now()
    read_file=(dt.second*1000000+dt.microsecond-start)/1000
    ############################################
    dy=dt.second*1000000+dt.microsecond
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
            flag=int(date[1])
            if flag <7:
                if   flag == 1:
                    pom = 0
                elif flag == 2:
                    pom = 31
                elif flag == 3:
                    pom = 60
                elif flag == 4:
                    pom = 91
                elif flag == 5:
                    pom = 121
                elif flag == 6:
                    pom = 152
            else:
                if flag == 7:
                    pom = 182
                elif flag == 8:
                    pom = 213
                elif flag == 9:
                    pom = 244
                elif flag == 10:
                    pom = 274
                elif flag == 11:
                    pom = 305
                elif flag == 12:
                    pom = 335
                
            if len(date) > 2:
                pom=pom+int(date[2])
            else:
                pom = -1
        else:
            pom = -2

        row = []
        for val in date:
            row.append(val)
        for k in range(1,len(temp)):
            row.append(temp[k])
        row.append(str(pom))
        #print(row)
        table.append(row)
    #print(table)
    dt = datetime.now()
    dy=(dt.second*1000000+dt.microsecond-dy)/1000
    """
    tmpstr=""
    for m in range(0,len(table)-1):
        for n in range(0,len(table[0])):
            tmpstr+=table[m][n]+"\t"
            #print(table[m][n]+"\t", end="")
        #print("")
        tmpstr+="\n"
    #print(tmpstr)
    """
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    #print("Read file: ",read_file," miliseconds")
    #print("Add dayoy: ",dy," miliseconds")
    #print("Sta t end: ",fin," miliseconds\n")
    return table,year

def process_data_env(q,url,year,city,country):
    q.put(process_data(url,year,city,country))

                
def process_data_all_mt(city):
    q = queue.Queue()
    table = [[] for j in range(0,116)]
    #table = []
    flag = True
    count_to_flag = 0
    year=2015
    
    while year >= 1900:
        url="http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
        dt = datetime.now()
        op=(dt.minute*60+dt.second)*1000000+dt.microsecond
        ######################
        t = threading.Thread(target=process_data_env, args = (q,url,year,city[0],city[2]))
        t.daemon = True
        t.start()
        ########MULTY#########
        dt = datetime.now()
        op=(dt.minute*60+dt.second)*1000000+dt.microsecond-op
        year-=1
    #
    qlen=116
    while qlen>0 and flag:
        s = q.get()
        table[115-(s[1]-1900)]=s[0]
        #table.append(s[0])
        #print(s[1])
        qlen-=1
        if len(s[0]) < 1:
            count_to_flag+=1
        else:
            count_to_flag = 0
        if  count_to_flag > 20:
            flag = False
    #print("TABLE: ",len(table))
    return table
        
def process_data_all_st(city):
    table = []
    flag = True
    count_to_flag = 0
    year=2015
    
    while flag:
        url="http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
        dt = datetime.now()
        op=(dt.minute*60+dt.second)*1000000+dt.microsecond
        temp,year = process_data(url,year,city[0],city[2])
        dt = datetime.now()
        op=(dt.minute*60+dt.second)*1000000+dt.microsecond-op
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
    return table
        
