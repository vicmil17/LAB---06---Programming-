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

# ----------------------------------------------------------
#Part 4 - Visualizing statistical relationships
# ----------------------------------------------------------

import matplotlib.pyplot as plt

# Scatter plot for females
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, female")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()

# Scatter plot for males
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, male")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()

# ----------------------------------------------------------
#Step 1: relplot() with color by Region
# ----------------------------------------------------------
# Female life expectancy by region
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",             # color-coded by region
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, female by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()

# Male life expancy by region 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, male by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()

# ----------------------------------------------------------
#Step 2: relplot() with Lines and Standard Deviation
# ----------------------------------------------------------
#For women
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
    kind="line",
    ci="sd",        # show standard deviation as shaded area
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, female by Region — Line + SD")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()

#For men 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    kind="line",
    ci="sd",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, male by Region — Line + SD")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()
# ----------------------------------------------------------
#lmplot() — Linear Regression per Region
# ----------------------------------------------------------
#for women 
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
    height=5,
    aspect=1.3,
    scatter_kws={"alpha":0.6})
plt.title("Linear Regression: GNI per Capita vs Life expectancy, female by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()

#for men
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    height=5,
    aspect=1.3,
    scatter_kws={"alpha":0.6})
plt.title("Linear Regression: GNI per Capita vs Life expectancy, male by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()

#This part explores the relationship between a country's income level,
#(GNI per capita) and life expectancy, with separate plots for men and women.
