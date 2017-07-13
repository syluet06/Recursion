import time
def josephus(person):
    if person==1 or person==2:
        return 1
    else:
        if person%2 is 0:
            return 2*josephus(person/2)+1
        else:
            return 2*josephus((person+1)/2)-1

for person in range(100):
    print str(person) + " " + str(josephus(person+1))
    time.sleep(1)
