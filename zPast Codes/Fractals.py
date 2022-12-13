'Given a pattern, recreate the pattern recursively similar to how snowflakes works'
n, k = [int(x) for x in input().split()]
fractal = ['' for x in range(n)]
for x in range(n):
    fractal[x] += input()
def fractalize(orig, new, n, size):
    new_fractal = ['' for x in range(n*size)]
    for x in range(size):
        for y in range(size):
            if new[x][y] == ".":
                for z in range(n):
                    new_fractal[n*x+z] += orig[z]
            else:
                for z in range(n):
                    new_fractal[n*x+z] += n*'*'
    return new_fractal
ans = fractal.copy()
for x in range(k-1):
    ans = fractalize(fractal, ans, n, n**(x+1))
for x in ans:
    print(''.join(x))
