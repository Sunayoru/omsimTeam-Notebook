def modinv(a,m):
  x, y = 1, 1
  g, x, y = extended_euclid(a, m, x, y)
  if g == 1 or g == -1: return mod(x * g, m)
  return 0 # 0 if invalid
