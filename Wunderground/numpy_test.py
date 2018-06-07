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
import colorsys
import numpy

ofc = datetime.now()
ofc_s=ofc.second*1000000+ofc.microsecond
############################################
a=[0 for i in range(0,10000000)]
############################################
ofc = datetime.now()
ofc_f=float(ofc.second*1000000+ofc.microsecond-ofc_s)/1000
print("List ",ofc_f," milliseconds")

ofc = datetime.now()
ofc_s=ofc.second*1000000+ofc.microsecond
############################################
#X = numpy.arange(10000000,dtype=numpy.uint8)
X = numpy.zeros(10000000,dtype=numpy.uint8)
############################################
ofc = datetime.now()
ofc_f=float(ofc.second*1000000+ofc.microsecond-ofc_s)/1000
print("Numpy ",ofc_f," milliseconds")

ofc = datetime.now()
ofc_s=ofc.second*1000000+ofc.microsecond
############################################

#B = list(bytes(X))
B = bytes(X)
ofc = datetime.now()
ofc_f=float(ofc.second*1000000+ofc.microsecond-ofc_s)/1000
print("To bytes conversion time ",ofc_f," milliseconds")
print(len(B))
"""
for i in range(0,258):
    print(B[i].numerator)



for i in range(0,258):
    print(X[i])

"""
