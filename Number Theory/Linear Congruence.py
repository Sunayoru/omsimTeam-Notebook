def linconsolver(a, b, m):
  x, y = 1, 1
  g, x, y = extended_euclid(a, m, x, y)
  if b % g != 0: return (-1, -1)
  return (mod(x*b/g, m/g), abs(m/g))
