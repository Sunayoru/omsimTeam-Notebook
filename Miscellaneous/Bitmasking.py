#Given an array of n integers and an integer x, how many subsets
#have a sum equal to x?
def subset_sum(a,n,x):
  ctr = 0
  for mask in range(1<<n): # for each subset
    total = 0
    for i in range(n):
      if mask&(1<<i): # include ith element?
        total += a[i]
      if total == x:
        ctr += 1

  return ctr
