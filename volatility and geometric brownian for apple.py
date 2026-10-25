# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:15:56 2026

@author: santo
"""





import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

"Apple stock data"
ticker = "AAPL"

data = yf.download(
    ticker,
    start="2025-01-01",
    end="2026-01-01",
    auto_adjust=True
)



close = data["Close"]
if isinstance(close, __import__("pandas").DataFrame):
    close = close.iloc[:, 0]

# 2. Plot stock value as a function of time
plt.figure(figsize=(12, 6))
plt.plot(close.index, close.values, linewidth=1.5)

plt.xlabel("Date")
plt.ylabel("Apple stock price (USD)")
plt.title("Apple (AAPL) Stock Price in 2025")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


returns = close.pct_change().dropna()

daily_volatility = returns.std()
annualized_volatility = daily_volatility * np.sqrt(252)

print("Apple (AAPL) — 2025")
print(f"Number of daily prices: {len(close)}")
print(f"Daily volatility: {daily_volatility:.4%}")
print(f"Annualized volatility: {annualized_volatility:.4%}")
print(f"Mean daily return: {returns.mean():.4%}")
print(f"Total price return: {(close.iloc[-1] / close.iloc[0] - 1):.2%}")



"Multiple possible pathss"


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


ticker = "AAPL"

data = yf.download(ticker,start="2025-01-01",end="2026-01-01",auto_adjust=True)

close = data["Close"]
if isinstance(close, __import__("pandas").DataFrame):
    close = close.iloc[:, 0]

close = close.dropna()
log_returns = np.log(close / close.shift(1)).dropna()

# -----------------------------
# 2. Estimate model parameters
# -----------------------------
trading_days = 252
dt = 1 / trading_days

# Annualized historical drift and volatility
mu = log_returns.mean() * trading_days
sigma = log_returns.std() * np.sqrt(trading_days)

S0 = float(close.iloc[0])
n_steps = len(close) - 1
n_paths = 10

# Binomial up/down factors
u = np.exp((mu - 0.5 * sigma**2) * dt
           + sigma * np.sqrt(dt))
d = np.exp((mu - 0.5 * sigma**2) * dt
           - sigma * np.sqrt(dt))

p = 0.5

print(f"Starting price: ${S0:.2f}")
print(f"Annualized drift: {mu:.2%}")
print(f"Annualized volatility: {sigma:.2%}")
print(f"Up factor: {u:.5f}")
print(f"Down factor: {d:.5f}")
print(f"Probability of up move: {p:.2f}")

# -----------------------------
# 3. Simulate trajectories
# -----------------------------
np.random.seed(42)

paths = np.zeros((n_steps + 1, n_paths))
paths[0, :] = S0

for t in range(1, n_steps + 1):
    random_moves = np.random.rand(n_paths) < p
    factors = np.where(random_moves, u, d)
    paths[t, :] = paths[t - 1, :] * factors

# -----------------------------
# 4. Plot all trajectories
# -----------------------------
time = np.arange(n_steps + 1)

plt.figure(figsize=(12, 6))

for i in range(n_paths):
    plt.plot(time, paths[:, i], alpha=0.5, linewidth=1)

# to compare to actual data
plt.plot(np.arange(len(close)),close.values,color="black",linewidth=2,label="Actual data")

plt.xlabel("Trading days since start")
plt.ylabel("Stock price")
plt.title("Apple: Binomial Model ")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()



