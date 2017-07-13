def fibonacci(n):
    if n<=1:
        return 1;
    else:
        return fibonacci(n-1)+fibonacci(n-2);

for i in range(10):
    print("fibonacci(%d):%d" % (i+1,fibonacci(i+1)))
