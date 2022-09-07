# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:55:12 2022

@author: siirias
"""
import sklearn as skl
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset
import xarray as xr
import pandas as pd
import re
import argopy

indir = "C:/Data/ArgoData/ArgosForPlot/RBR_BalticProper/"
infiles = ["GL_PR_PF_6903706.nc", "GL_PR_PF_3902110.nc",
            "GL_PR_PF_6904116.nc", "GL_PR_PF_6904117.nc", 
            "GL_PR_PF_6904226.nc", "GL_PR_PF_7900587.nc"]


#first, load the dataset:
for filename in infiles:
    with xr.open_dataset(indir + filename) as f:
        print(f['PSAL'])
