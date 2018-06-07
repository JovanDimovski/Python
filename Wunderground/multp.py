from multiprocessing import Pool
import sys
import time

def f(x):
    k,l=x
    
    return k*l

if __name__ == '__main__':
    p = Pool(2)
    print(p.map(f, [(1,2),(3,4)]))
    time.sleep(5)
