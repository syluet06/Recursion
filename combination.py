def C(a,b):
    if b is 0 or a is b:
        return 1
    elif b is 1 or a is b+1:
        return a
    else:
        return C(a-1,b-1)+C(a-1,b)

for i in range(6):
    for k in range (i):
        print("C(%s,%s):%s" % (i,k,C(i,k)))
