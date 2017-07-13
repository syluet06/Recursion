def reverse(s):
    if len(s) is 1:
        return s
    else:
        return s[-1]+reverse(s[0:-1])

print("%s:%s" % ("soner",reverse("soner")))
