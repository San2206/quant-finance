# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 02:06:26 2026

@author: santo
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



S0 = 100.0
K = 100.0
sigma = 0.20
r = 0.05
T = 1.0

N = 200_000       # Number of MC paths
seed = 42   # This is something that the random number generator needs

# Finite-difference steps
dS = 0.5
dSigma = 0.005
dt = 1.0 / 365.0

rng = np.random.default_rng(seed)
Z = rng.standard_normal(N)



# Black holes and greeks


def bs_price(S, K, sigma, T, r):
    if T <= 0:
        return max(S - K, 0.0)

    d1 = (np.log(S / K) + (r + 0.5*sigma**2) * T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)


def bs_greeks(S, K, sigma, T, r):
    d1 = (np.log(S / K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S*sigma*np.sqrt(T))

    vega = S*norm.pdf(d1)*np.sqrt(T)

    theta = (-S*norm.pdf(d1)*sigma / (2*np.sqrt(T))- r * K * np.exp(-r * T) * norm.cdf(d2))

    return delta, gamma, vega, theta



# mc stuff


def mc_price(S, sigma, T, Z):
    ST = S*np.exp((r - 0.5 * sigma**2) * T+ sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0.0)

    return np.exp(-r * T) * np.mean(payoff)

C_mc = mc_price(S0, sigma, T, Z) #base price



# Delta: dC/dS
C_up = mc_price(S0 + dS, sigma, T, Z)
C_down = mc_price(S0 - dS, sigma, T, Z)

delta_mc = (C_up - C_down) / (2 * dS)

# Gamma: d2C/dS2
gamma_mc = (C_up - 2 * C_mc + C_down) / dS**2

# Vega: dC/dsigma
C_vol_up = mc_price(S0, sigma + dSigma, T, Z)
C_vol_down = mc_price(S0, sigma - dSigma, T, Z)

vega_mc = (C_vol_up - C_vol_down) / (2 * dSigma)

# Theta: dC/dt
C_longer = mc_price(S0, sigma, T + dt, Z)
C_shorter = mc_price(S0, sigma, T - dt, Z)

theta_mc = -(C_longer - C_shorter) / (2 * dt)



# to compare with black scholes


C_bs = bs_price(S0, K, sigma, T, r)

delta_bs, gamma_bs, vega_bs, theta_bs = bs_greeks(S0, K, sigma, T, r)



names = ["Call Price", "Delta", "Gamma", "Vega", "Theta"]

mc_values = [C_mc, delta_mc, gamma_mc, vega_mc, theta_mc]

bs_values = [C_bs, delta_bs, gamma_bs, vega_bs, theta_bs]

print("\nMonte Carlo vs Black-Scholes")
print("=" * 67)
print(f"{'Quantity':<15}{'Monte Carlo':>16}{'Black-Scholes':>18}{'Abs. Error':>15}")
print("-" * 67)

for name, mc, bs in zip(names, mc_values, bs_values):
    print(f"{name:<15}{mc:>16.6f}{bs:>18.6f}{abs(mc-bs):>15.6f}")


