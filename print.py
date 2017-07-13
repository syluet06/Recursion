def printw(s,current,start):
    if(current!=start):
        printw(s,current-1,start)
    print(s[current])

printw("soner",4,0)
