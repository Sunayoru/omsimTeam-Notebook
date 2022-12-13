def mod(x, m):
  if m == 0: return 0
  if m < 0: m *= -1
  return (x%m + m) % m
def extended_euclid(a, b, x, y):
  if b == 0:
    x = 1
    y = 0
    return a, x, y
  g, x, y = extended_euclid(b, a%b, x, y)
  z = x - a//b*y
  x = y
  y = z
  return g, x, y
