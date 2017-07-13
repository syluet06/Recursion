def hanoi(n,source,spare,destination):
    if n is 0:
        return
    else:
        hanoi(n-1,source,spare,destination)
        print("%s > %s" % (source,spare))
        hanoi(n-1,destination,spare,source)
        print("%s > %s" % (spare,destination))
        hanoi(n-1,source,spare,destination)

for i in range(3):
    print(str(i+1))
    hanoi(i+1,"A","B","C")
