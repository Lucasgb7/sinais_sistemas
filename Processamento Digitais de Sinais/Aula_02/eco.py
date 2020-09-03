# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:48:03 2020

@author: lucas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Fs = 8000
t1 = 1 * 10**-3 
t2 = 1.5 * 10**-3
n1 = t1*Fs
n2 = t2*Fs
# Ganhos
a = [.5, .3, .2]
delay_length = n2
vector_delay = np.zeros(delay_length)
# Entradas
enter = np.zeros(2*delay_length)
index = np.where(enter==0)
enter[index] = 1
