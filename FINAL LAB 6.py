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

print(data.nunique())
#Get descriptive statistics for all numeric columns
print(data.describe())
# Add a new column for GNI per capita
data["GNI per capita"] = data["GNI"] / data["Population"]
data["GNI per capita"] = data["GNI per capita"].round(2)
# a) Count how many countries are in each region
print(data["Region"].value_counts())
# b) How many high income economies are there?
print(data["High Income Economy"].value_counts())
# Where are the high income economies (per region)?
table = pd.crosstab(data["Region"], data["High Income Economy"])
print(table)
# Create empty lists
countries_over_80 = []

# Loop through the dataset row by row
for i in range(len(data)):
    if data["Life expectancy, female"][i] > 80:
        countries_over_80.append(data["Country Name"][i])
print("Number of countries where women live more than 80 years:", len(countries_over_80))
print("Countries:", countries_over_80)



