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

plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 20)
plt.scatter(normal['elongation'], normal['sphericity'], s = 30, c = 'r', marker = 'o')
plt.scatter(thin['elongation'], thin['sphericity'], s = 30, c = 'b', marker = 's')
plt.scatter(mnist['elongation'], mnist['sphericity'], s = 30, c = 'g', marker = '*')
plt.scatter(mostly['elongation'], mostly['sphericity'], s = 30, c = 'm', marker = 'P')
plt.legend(['Normal', 'Thin', 'MNIST', 'Mostlyconvex'], markerscale = 2.5)
plt.xlabel('Elongation')
plt.ylabel('Roundness')
plt.savefig('roundness-elongation.png')
