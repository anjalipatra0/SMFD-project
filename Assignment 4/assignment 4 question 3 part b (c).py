from scipy.stats import norm
from scipy.integrate import quad
import numpy as np

mean = 100
sigma = np.sqrt(15.708)
K = 105

def integrand(S):
    return (S - K) * norm.pdf(S, loc=mean, scale=sigma)

expected_payoff, _ = quad(integrand, K, np.inf)
print("Expected Payoff:", expected_payoff)
