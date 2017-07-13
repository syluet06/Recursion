def binary(s):
    if s is 0:
        return ""
    else:
        return str(s%2)+binary(int(s/2))


a = input()
print("%s:%s" % (a,binary(a)[::-1]))
