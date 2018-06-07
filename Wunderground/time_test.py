
"""
import os
import urllib3
from datetime import datetime

def get_data(url):
    r = urllib3.PoolManager().request('GET', url)
    r=r.data.decode('utf-8')  
    return r

for year in range(2010,2015):
    url="http://www.wunderground.com/history/airport/LWSK/"+str(year)+"/1/1/CustomHistory.html?dayend=31&monthend=12&yearend="+str(year)+"&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1"
    dt = datetime.now()
    start=dt.second*1000000+dt.microsecond
    ############################################
    get_data(url)
    ############################################
    dt = datetime.now()
    fin=float(dt.second*1000000+dt.microsecond-start)/1000
    print("Time to retrieve file: ",fin," milliseconds")

"""

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

q = queue.Queue()
countries = []
countries.append("US")
cities=weather_codes.get_cities(countries)
print("CITIES: ",len(cities))
urls = []
for city in cities:
    for year in range(1915,2015):
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
print("URLS: ",len(urls))

for city in cities:
    print(city)
##    
##for url in urls:
##    print(url)
##
num_urls = len(urls)
batches = int(num_urls/500)
ibc =0
obc =0
auc = obc*500+ibc
while auc < num_urls:
    #print(auc)
    ibc = 0
    #for url in urls:
    while ibc < 500 and auc < num_urls:
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
    cnt = 0
    #for url in urls:
    ibc = 0
    while ibc < 500 and auc < num_urls:
        url=urls[auc]
        s = q.get()
        cnt+=1
        if cnt%100 == 0:
            print(cnt)
            #print("\n",s[1],s[3],s[2],"\n",s[0][394:480],"\n\n")
            print(s[1],s[3],s[2],"\n")
        directory = "C:/Python34/Scripts/WeatherData/"+url[1]+"/"+url[2]+"/"
        filepath  = "C:/Python34/Scripts/WeatherData/"+url[1]+"/"+url[2]+"/"+str(url[3])+".txt"
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

