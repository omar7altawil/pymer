import time

def starttimer():
     global pymerT1 
     pymerT1 =time.time()

def endtime():
    print(str((time.time()-pymerT1)*1000)+ "ms")

