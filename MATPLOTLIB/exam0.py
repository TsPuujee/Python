#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:24:10 2018

@author: geeks

0. install numpy ( sudo apt install python-numpy OR sudo pip install numpy)
1. install matplotlib (sudo apt install python-matplotlib OR sudo pip install matplotlib)
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()
