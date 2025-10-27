# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:09:47 2025

@author: Olivia Maragos and Victoria Milioto 
"""

import pandas as pd
import seaborn as sns
print(sns.__version__)
data = pd.read_csv("wdi_wide.csv")

# ----------------------------------------------------------
#Part 3 – Understanding and preparing the data
#Answer the question: how many empty values for the column “Physicians” and “Population”?
print("Missing values in Physicians:", data["Physicians"].isnull().sum())
print("Missing values in Population:", data["Population"].isnull().sum())

# ----------------------------------------------------------
#nunique counts how many different entries exist per column.
# ----------------------------------------------------------



