import numpy as np

N = 100000
daily_moves = np.random.uniform(-2, 2, size=(N, 10))
final_prices = 100 + np.sum(daily_moves, axis=1)
payoffs = np.maximum(final_prices - 105, 0)

fair_value = np.mean(payoffs)
print("Estimated Fair Value:", fair_value)
