#!/usr/bin/env python3
"""Markov chain — simulation, stationary distribution, absorption."""
import random

class MarkovChain:
    def __init__(self, trans):
        self.trans = trans; self.states = list(trans.keys())
    def step(self, state):
        r = random.random(); cumsum = 0
        for next_state, prob in self.trans[state].items():
            cumsum += prob
            if r <= cumsum: return next_state
        return self.states[-1]
    def simulate(self, start, n):
        path = [start]
        for _ in range(n): path.append(self.step(path[-1]))
        return path
    def stationary(self, tol=1e-8, max_iter=10000):
        n = len(self.states); idx = {s:i for i,s in enumerate(self.states)}
        pi = [1/n]*n
        for _ in range(max_iter):
            new_pi = [0]*n
            for i, s in enumerate(self.states):
                for t, p in self.trans[s].items():
                    new_pi[idx[t]] += pi[i] * p
            if max(abs(new_pi[i]-pi[i]) for i in range(n)) < tol: break
            pi = new_pi
        return {s: pi[i] for i, s in enumerate(self.states)}

def main():
    mc = MarkovChain({"A":{"A":0.7,"B":0.3},"B":{"A":0.4,"B":0.6}})
    print(f"Stationary: {mc.stationary()}")

if __name__ == "__main__": main()
