def totient(n):
  if n <= 1: return 1
  tot = n
  for i in range(2, n):
    if i*i > n: break
    if n % i == 0: tot -= tot/i
    while n % i == 0: n /= i
  if n > 1: tot -= tot / n
  return int(tot)
