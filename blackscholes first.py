# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 23:52:29 2026

@author: santo
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ==================================================
# Black-Scholes European Call Option
# ==================================================

def black_scholes_call(S0, K, sigma, t, r):
    """
    S0    : Initial stock price
    K     : Strike price
    sigma :volatility
    t     : Time to maturity 
    r     : risk-free interest rate
    """

    if t <= 0:
        return max(S0 - K, 0)
    if sigma == 0:
        return max(S0 - K * np.exp(-r * t), 0)

    d1 = (np.log(S0 / K)+ (r + 0.5 * sigma**2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    C0 = (S0 * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2))
    return C0


S0 = 100       # Initialprice
K = 100        # Strike price
sigma = 0.20   # volatility 
r = 0.05       # Risk-free interest rate 


# Calculate option price as a function of time

times = np.linspace(0.001, 2.0, 500)

call_prices = np.array([
    black_scholes_call(S0, K, sigma, t, r)
    for t in times])



plt.figure(figsize=(10, 6))
plt.plot(times, call_prices, linewidth=2,
         label="BlackScholes Call Price")
plt.xlabel("Time, t ", fontsize=12)
plt.ylabel("Call option price $C_0$", fontsize=12)

plt.title("Black-Scholes Call Price vs Time to Maturity",
          fontsize=14)

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# ==================================================
# Print example option prices
# ==================================================

print("Black-Scholes European Call")

for t in [0.25, 0.5, 1.0, 1.5, 2.0]:
    price = black_scholes_call(S0, K, sigma, t, r)
    print(f"Maturity time = {t:.2f} years: C0 = {price:.4f}")
