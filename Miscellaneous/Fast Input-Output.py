import sys
input = sys.stdin.readline
input().rstrip('\r\n')
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
input().decode().rstrip("\r\n")
# normal print()
sys.stdout.write(str(n) + "\n")
# print list, print(*list)
sys.stdout.write(" ".join(map(str,list)) + "\n")
