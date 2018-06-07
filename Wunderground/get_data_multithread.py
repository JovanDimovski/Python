import time
import queue
import threading
import urllib3
import os
from datetime import datetime

import weather_codes


dt = datetime.now()
start=(dt.minute*60+dt.second)*1000000+dt.microsecond
############################################


# called by each thread
def get_url(q, url, year, city, country):
    q.put([urllib3.PoolManager().request('GET', url).data.decode('utf-8'),year,city,country])

def fetch_data_multithread(cities,starty,endy):
    more = True
    while more:
        more = fetch_data_multithread_inside(cities,starty,endy)
        if more is True:
            print ("Restarting.. .  .    .")
            for i in range(1,10):
                time.sleep(1) 
                print(i)

def fetch_data_multithread_inside(cities,starty,endy):
    q = queue.Queue()
    
    urls = []
    for city in cities:
        for year in range(int(starty),int(endy)):
            #print(city)
            directory = "C:/Python34/Scripts/WeatherData/"+city[2]+"/"+city[0]+"/"
            filepath  = "C:/Python34/Scripts/WeatherData/"+city[2]+"/"+city[0]+"/"+str(year)+".txt"
            if not os.path.exists(directory):
                #os.makedirs(directory)
                #APPEND#
                pom = []
                pom.append("http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1")
                pom.append(city[2])
                pom.append(city[0])
                pom.append(year)
                urls.append(pom)
            else:
                if not os.path.isfile(filepath):
                    #APPEND#
                    pom = []
                    pom.append("http://www.wunderground.com/history/airport/"+city[1]+"/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1")
                    pom.append(city[2])
                    pom.append(city[0])
                    pom.append(year)
                    urls.append(pom)
                #else:
                    #DO NOT APPEND TO LIST OF URLS#
                    print("File Already Exists.\n")
                    
    #for url in urls:
    #    print(url)
    print("Urls to fetch: ",len(urls))
    print("Already have: ",str(len(cities)*(endy-starty)-len(urls)))
    if len(urls) == 0:
        return False
    #for city in cities:
    #    print(city)
    ##    
    ##for url in urls:
    ##    print(url)
    ##
    num_urls = len(urls)
    batches = int(num_urls/500)+1
    print("BATCHES: ",batches)
    ibc =0
    obc =0
    auc = obc*500+ibc
    cnt = 0
    lcnt = 0
    l_sec = datetime.now().hour*3600+datetime.now().minute*60+datetime.now().second
    c_sec = datetime.now().hour*3600+datetime.now().minute*60+datetime.now().second
    while obc < batches:
        print("Batch num: ",obc)
        c_sec = datetime.now().hour*3600+datetime.now().minute*60+datetime.now().second
##        if c_sec >= (l_sec+10):
##            l_sec = c_sec
##            print(c_sec,"\t",cnt)
        #print(auc)
        ibc = 0
        auc = obc*500+ibc
        #for url in urls:
        while ibc < 500 and auc < num_urls:
            c_sec = datetime.now().hour*3600+datetime.now().minute*60+datetime.now().second
##            if c_sec >= (l_sec+10):
##                l_sec = c_sec
##                print(c_sec,"\t",cnt)
            #print(auc)
            url=urls[auc]
            t = threading.Thread(target=get_url, args = (q,url[0],url[3],url[2],url[1]))
            t.daemon = True
            t.start()
            ibc+=1
            auc = obc*500+ibc
        #print(obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,)
        #print(obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,)
        #print(obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,)
        #print(obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,obc,)
        
        #for url in urls:
        ibc = 0
        auc = obc*500+ibc
        
        time.sleep(5)
        while ibc < 500 and auc < num_urls:
            c_sec = datetime.now().hour*3600+datetime.now().minute*60+datetime.now().second
            if c_sec >= (l_sec+10):
                l_sec = c_sec
                print(c_sec,"\t",cnt)
                if cnt <= lcnt+50:
                    print("To few threads returned.")
                    q.queue.clear()
                    return True
                lcnt=cnt
                
            #print(auc)
            #url=urls[auc]
            try:
                s = q.get()
            except TimeoutError:
                print("Thread timed out")
            cnt+=1
            #if cnt%100 == 0:
            #    print(cnt)
                #print("\n",s[1],s[3],s[2],"\n",s[0][394:480],"\n\n")
            #
            #print(s[0][394:480],s[1],s[2],s[3],"\n")
            directory = "C:/Python34/Scripts/WeatherData/"+s[3]+"/"+s[2]+"/"
            filepath  = "C:/Python34/Scripts/WeatherData/"+s[3]+"/"+s[2]+"/"+str(s[1])+".txt"
            if not os.path.exists(directory):
                os.makedirs(directory)
            #print(os.path.isfile(filepath))
            if os.path.isfile(filepath):
                #GET_DATA_FROM_FILE#
                f = open(filepath, 'r')
                r = f.read()
                f.close()
            else:
                #STORE_DATA_TO_FILE#
                r=s[0]
                f = open(filepath, 'w')
                f.write(r)
                f.close()
            ibc+=1
            auc = obc*500+ibc
        obc+=1     

    ############################################
    dt = datetime.now()
    fin=float((dt.minute*60+dt.second)*1000000+dt.microsecond-start)/1000

    estr= " milliseconds"
    if fin > 1000:
        fin = fin/1000
        estr= " seconds"
    print("Time to retrieve files: ",fin,estr)
    return False



"""
countries = []
countries.append("MK")
cities=weather_codes.get_cities(countries)
#print("CITIES: ",len(cities))
fetch_data_multithread(cities,2000,2006)
"""
