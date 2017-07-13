from array import *
def sum(a):
    if len(a) is 1:
        return a[0]
    else:
        new = array("i")
        for i in range(len(a)-2):
            new.insert(i,a[i])
        new.append(a[-1]+a[-2])
    return sum(new)

a = array("i", [100,300,500,400,20,36])
print(str(sum(a)))
