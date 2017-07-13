def hanoi(n,source,destination,subs):
    if n is 1:
        print("%s > %s" % (source,destination))
    else:
        hanoi(n-1,source,subs,destination)
        print("%s > %s" % (source,destination))
        hanoi(n-1,subs,destination,source)

for i in range(3):
    print(str(i+1))
    hanoi(i+1,"A","C","B")
