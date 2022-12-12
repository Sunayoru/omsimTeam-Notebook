def generate_is_prime_sieve_opt(N):
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p*p <= N:
        if is_prime[p]:
            for n in range(p*p, N+1, p):
                is_prime[n] = False
        p += 1
    return is_prime
is_prime = generate_is_prime_sieve_opt(int(input()))
