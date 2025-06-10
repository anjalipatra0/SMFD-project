
import numpy as np

def simulate_stock_price(start_price, target_price, steps, simulations):
    success_count = 0
    for _ in range(simulations):
        price = start_price
        for _ in range(steps):
            move = np.random.choice([0.01, 0, -0.01], p=[0.1, 0.85, 0.05])
            price += move
            if price >= target_price:
                success_count += 1
                break
    return success_count / simulations

# Parameters
start_price = 120
target_price = 130
steps = 2160
simulations = 10000

probability = simulate_stock_price(start_price, target_price, steps, simulations)
print("Probability:", probability)
