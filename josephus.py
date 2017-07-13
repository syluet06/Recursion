def josephus(person):
    if person==1 or person==2:
        return 1
    else:
        if person%2 is 0:
            return 2*josephus(person/2)+1
        else:
            return 2*josephus((person+1)/2)-1

for person in range(20):
    print str(person+1) + " " + str(josephus(person+1))
    
