def longest_increasing_subsequence(numbers):
    tails = [0] * len(numbers)
    size = 0
    for x in numbers:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] <= x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size
