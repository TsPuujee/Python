#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:24:10 2018

@author: geeks

exam0.py сайжруулав.
"""
import numpy as np
import matplotlib.pyplot as plt

# Хэмжээ нягтаршилийг тохируулж байна.
plt.figure(figsize=(8,6), dpi=100)

# subplot үүсгэх 
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Косинусийн графикийн өнгөb хэмжээ, хэлбэрийг тохируулж байна.
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# синусийн графикийн өнгө, хэмжээ, хэлбэрийгтохируулж байна.
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# X тэнхлэгийг тохируулж байна.
plt.xlim(-4.0,4.0)
plt.xticks(np.linspace(-4,4,9,endpoint=True))

# Y  тэнхлэгийг тохируулж байна.
plt.ylim(-1.0,1.0)
plt.yticks(np.linspace(-1,1,5,endpoint=True))

plt.show()
