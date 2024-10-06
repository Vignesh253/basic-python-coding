import time
myt = int (input ("entrt the time in seconds"))


for x in (range(myt,0,-1)):
    sec=x%60
    min=int(x/60)%60
    hrs=int(x/3600)
    print (f"{sec:02}:{min:02}:{hrs:02}")
    time.sleep(1)

print("up!!!!!!!!!!")   
