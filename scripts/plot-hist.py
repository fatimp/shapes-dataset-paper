#!/usr/bin/env python

import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

with sqlite3.connect('glyphs.db') as db:
    data = pd.read_sql_query('select * from pores where lfer > 0.9', db)

normal = data.query('name == "handmade/"')
mnist  = data.query('name == "glyphs/"')
thin   = data.query('name == "handmade3/"')
mostly = data.query('name == "mostlyconvex-gan/"')

def factor(data):
    return (data['elongation'] + data['sphericity']) / 2

fnormal = factor(normal)
fthin   = factor(thin)
fmnist  = factor(mnist)
fmostly = factor(mostly)

def countfactors(factors, min, max):
    a = np.where(min <= factors, 1, 0)
    b = np.where(factors < max, 1, 0)
    return np.sum(a * b)

def calchist(factors):
    return np.array([countfactors(factors, 0.2, 0.4),
                     countfactors(factors, 0.4, 0.6),
                     countfactors(factors, 0.6, 0.8),
                     countfactors(factors, 0.8, 1.0)])

hnormal = calchist(fnormal)
hthin   = calchist(fthin)
hmnist  = calchist(fmnist)
hmostly = calchist(fmostly)
xs = [
    'Elongated\ndissected',
    'Isometric\ndissected',
    'Isometric\nslightly\ndissected',
    'Round'
]
ys = [hnormal, hthin, hmnist, hmostly]
bottom = np.zeros(len(xs))

plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 20)

for data in ys:
    plt.bar(xs, data, bottom = bottom)
    bottom = bottom + data

plt.legend(['Normal', 'Thin', 'MNIST', 'Mostlyconvex'], markerscale = 2.5)
plt.ylabel('Amount of shapes')
plt.savefig('shape-factor.png')
