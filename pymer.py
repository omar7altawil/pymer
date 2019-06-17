import time

def startTimer():
     global pymerT1 
     pymerT1 =time.time()

def endTime():
    print(str((time.time()-pymerT1)*1000)+ "ms")

