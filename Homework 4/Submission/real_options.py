import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom
from typing import Callable


def call_payoff(spot, strike):
    return np.maximum(spot - strike, 0.0)

def put_payoff(spot, strike):
    return np.maximum(strike - spot, 0.0)

def eu_binom_pricer(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float, nper: int, payoff: Callable) -> float:
    pass 
    h = expiry / nper
    u = np.exp((rate - div)*h + vol*np.sqrt(h))
    d = np.exp((rate - div)*h - vol*np.sqrt(h))
    pstar = (np.exp((rate - div)*h) - d) / (u - d)
    spot_t = 0.0
    call_t = 0.0
    nodes = nper + 1
    disc = np.exp(-rate * expiry)
    
    for t in range(nodes):
        spot_t = spot * (u ** (nper-t)) * (d ** t)
        call_t += payoff(spot_t, strike) * binom.pmf(nper-t,nper,pstar)
    
    return disc*call_t

##American Options

def amer_binom_pricer(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float, num: int, payoff: Callable) -> float:
    
    h = expiry / num 
    u = np.exp(((rate - div) * h) + vol * np.sqrt(h)) 
    d = np.exp(((rate - div) * h) - vol * np.sqrt(h))
    pu = (np.exp((rate - div) * h) - d) / (u - d)
    pd = 1 - pu
    disc = np.exp(-rate * h)
    dpu = disc * pu
    dpd = disc * pd
    
    nodes = num + 1
    Ct = np.zeros(nodes)
    St = np.zeros(nodes)
    
    
    for i in range(nodes):
        St[i] = spot * (u ** (num - i)) * (d ** i)
        Ct[i] = payoff(St[i], strike)

        
    for i in range((num - 1), -1, -1):
        for j in range(i+1):
            Ct[j] = dpu * Ct[j] + dpd * Ct[j+1]
            St[j] = St[j] / u
            Ct[j] = np.maximum(Ct[j], payoff(St[j], strike))

    return Ct[0]

##black scholes options

def blk_sch_call(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float) -> float:
    d1 = (np.log(spot/strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))
    d2 = d1 - vol * np.sqrt(expiry) 
    d1_part = spot * np.exp(-div * expiry) * norm.cdf(d1)
    d2_part = strike * np.exp(-rate * expiry) * norm.cdf(d2)
    return d1_part-d2_part

def blk_sch_put(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float) -> float:
    d1 = (np.log(spot/strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))
    d2 = d1 - vol * np.sqrt(expiry) 
    d2_piece = (strike * np.exp(-rate * expiry) * norm.cdf(-d2))
    d1_piece = (spot * np.exp(-div * expiry) * norm.cdf(-d1))
    return  d2_piece-d1_piece


def binom_path(spot: float, expiry: float, rate: float, div: float, vol: float, nper: int) -> np.ndarray:
    h = expiry / nper
    u = np.exp((rate - div) * h + np.sqrt(h) * vol)
    d = np.exp((rate - div) * h - np.sqrt(h) * vol)
    pstar = (np.exp((rate - div) * h) - d) / (u - d) 
    z = np.random.uniform(size=nper)
    path = np.empty(nper)
    path[0] = spot

    for i in range(1, nper):
        if z[i] >= pstar: path[i] = u * path[i-1]
        else: z[i] = path[i] = d * path[i-1]

    return path



