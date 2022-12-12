def lcsubstring(X: str, Y: str,
                   m: int, n: int):
    LCSuff = [[0 for i in range(n + 1)]
                 for j in range(m + 1)]
    length = 0
    row, col = 0, 0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            else if X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if length < LCSuff[i][j]:
                    length = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0
    if length == 0:
        print("")
        return
    resultStr = ['0'] * length
    while LCSuff[row][col] != 0:
        length -= 1
        resultStr[length] = X[row - 1]
        row -= 1
        col -= 1
    print(''.join(resultStr))

lcsubstring(X, Y, m, n)
