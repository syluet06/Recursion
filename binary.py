def binary(s):
    if s is 0:
        return ""
    else:
        return binary(int(s/2))+str(s%2)


a = input()
print("%s:%s" % (a,binary(a)))
