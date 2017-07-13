import time
def power(a,b):
    if b is 0:
        return 1
    else:
        return a*power(a,b-1)

for i in range(10):
    for j in range(10):
        print("%s**%s:%s" % (j+1,i+1,power(j+1,i+1)))
        time.sleep(.3)
