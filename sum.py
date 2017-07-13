from array import *
def sum(array,index):
    if len(array) is index:
        return 0
    else:
        return array[index]+sum(array,index+1)

a = array('i', [1,5,6,3,98,15,245])
print(sum(a,0))
