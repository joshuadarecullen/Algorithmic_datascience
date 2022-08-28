import time
import numpy as np

def timeit(somefunc, *args, repeats=100,**kwargs):
    times=[]
    
    #excute function for the given repeats, timing the execution and obtaining the mean
    while repeats>0:
        starttime=time.time()
        ans=somefunc(*args,**kwargs)
        endtime=time.time()
        timetaken=endtime-starttime
        times.append(timetaken)
        repeats-=1
    
    mean=np.mean(times)
    stdev=np.std(times)
    error=stdev/(len(times)**0.5)
 
    return (ans,mean,error)
