
# Edmond takes total 2*n steps, n right and n up
# let x = number of right steps till now and y = number of up steps till now
# For our condition of not crossing the diagonal, y <= x 
# This is the same as the condition of finding the number of valid n parenthesis
# So, the answer for n, is Catalan number n

mod = 10**9 + 7
findtill = 100
dp = [0] * (findtill + 1)
dp[0] = 1

for n in range(1, findtill + 1):
    numerator = 2 * (2 * n - 1)
    denominator = n + 1

    # Recurrence relation used is C_n = ((2 * (2*n -1))/(n+1)) * C_n-1
    # for caculating modular inverse, fermat's little theorem is used

    inv_denominator = pow(denominator, mod - 2, mod)
    dp[n] = (dp[n-1] * numerator) % mod
    dp[n] = (dp[n] * inv_denominator) % mod

for n in range(1, 101):
    print(f"Number of paths P{n} = {dp[n]}")
