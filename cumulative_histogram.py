#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:03:24 2019

@author: saqlain
"""

import numpy as np

def cumulative_histogram(hist):
    cum_hist = hist.copy()
    
    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]
        
    return cum_hist