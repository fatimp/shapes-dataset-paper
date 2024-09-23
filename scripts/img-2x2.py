#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from PIL import Image
from PIL.ImageOps import invert

imgs = [
    Image.open('grains/handmade/0-up.pbm'),
    Image.open('grains/handmade/1-up.pbm'),
    Image.open('grains/handmade/2-up.pbm'),
    Image.open('grains/handmade/3-up.pbm')
]

#fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (8, 8), dpi = 300)
#fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
#for (img, ax) in zip(imgs, axes.flatten()):
#    ax.imshow(img)
#    ax.xaxis.set_major_locator(ticker.NullLocator())
#    ax.yaxis.set_major_locator(ticker.NullLocator())

fig = plt.figure(figsize = (8, 8), dpi = 300)
for i in range(4):
    ax = fig.add_subplot(2, 2, i+1)
    ax.imshow(invert(imgs[i]))
    ax.xaxis.set_major_locator(ticker.NullLocator())
    ax.yaxis.set_major_locator(ticker.NullLocator())

plt.subplots_adjust(wspace = 0.05, hspace = 0.05)
plt.savefig('test.png', bbox_inches='tight')
