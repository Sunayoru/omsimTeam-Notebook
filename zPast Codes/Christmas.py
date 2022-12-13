#recursion
n,x= [int(x) for x in input().split()]
layer = [1]
patty = [1]
for _ in range(1,51):
    layer.append(layer[_-1]*2 + 3)
    patty.append(patty[_-1]*2 + 1)
def eat(n, x):
    if n == 0:
        if x > 0:
            return 1
        else:
            return 0
    #check if in the lower half
    elif x < (layer[n]+1)//2:
        #eat the first bun then do the next recursion for the lowerhalf
        return eat(n-1, x-1)
    #check if in the middle
    elif x == (layer[n]+1)//2:
        return patty[n-1] + 1
    #check if in the upperhalf
    elif x > (layer[n]+1)//2:
        #do the recursion for the upperhalf then take the lowerhalf as eaten
        return eat(n-1, x-(layer[n]+1)//2) + patty[n-1] + 1
answer = eat(n, x)
print(answer)
