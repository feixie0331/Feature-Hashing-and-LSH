# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:29:41 2017

@author: fxie_
"""

from skimage import io,data
from skimage.color import rgb2gray
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  from skimage.transform import resize
import matplotlib.pyplot as plt
img1 = io.imread("hash1.PNG")
img2 = io.imread("hash2.PNG")
gimg1 = rgb2gray(img1)
gimg2 = rgb2gray(img2)
rimg1 = resize(gimg1,(9,8))
rimg2 = resize(gimg2,(9,8))

plt.figure(1)
plt.subplot(321)
plt.imshow(img1)
plt.subplot(322)
plt.imshow(img2)
plt.subplot(323)
plt.imshow(gimg1,cmap='gray')
plt.subplot(324)
plt.imshow(gimg2,cmap='gray')
plt.subplot(325)
plt.imshow(rimg1,cmap='gray')
plt.subplot(326)
plt.imshow(rimg2,cmap='gray')
plt.show()