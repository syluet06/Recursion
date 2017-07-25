def printw(s,current,start):
    if(current!=start):
        printw(s,current-1,start)
    print(s[current])

s = "i love recursion"
printw(s,len(s),0)
