from bisect import bisect_left
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
a  = [1, 2, 4, 4, 8]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
    #absent
else:
    #Prints first occurence, returns 2
