import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("Employee Dataset.csv")
# print(data.head())
# print(data.shape)
# print(data.info)
# print(data.index)
# print(data.columns)

# Creating a scatterplot with age and salary features

plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x="age", y="salary", color="blue", edgecolor='linen', alpha=0.5)
plt.title("Sactterplot of Age Vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
# plt.show()

# Observations-We can see there is a relationship between age and salary of employee,as the age increases salary increased as well,though some outliers are present.

# # Creating a scatterplot with healthy_eating and active_lifestyle features
#
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x="healthy_eating", y="active_lifestyle", color="red", edgecolor='linen', alpha=0.5)
plt.title("Sactterplot of Healthy Eating Vs Active Lifestyle")
plt.xlabel("Healthy Eating")
plt.ylabel("Active Lifestyle")
# plt.show()

# Observations-In general we can see there is a relationship between healthy eating and active lifestyle of employee,as the healthy eating increases active lifestyle increased as well,though some outliers are present.

# # Creating a scatterplot with healthy_eating and salary features
#
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x="healthy_eating", y="salary", color="k", edgecolor='linen', alpha=0.5)
plt.title("Sactterplot of Healthy Eating Vs Salary")
plt.xlabel("Healthy Eating")
plt.ylabel("Salary")
plt.show()

# Observation-same

# Creating a countplot for groups

plt.figure(figsize=(10, 5))
sns.countplot(data=data, x="groups",  edgecolor='linen', alpha=0.7)
plt.title("Countplot of groups")
plt.xlabel("Groups")
plt.ylabel("Count")
plt.show()

# Observation-Most employees belong to blood group A or O ,with A having most frequency

#Creating a histplot with salary features

plt.figure(figsize=(11, 6))
sns.histplot(data=data, x="salary", color="orange", edgecolor='linen', alpha=0.5,bins=10)
plt.title("Histplot of Salary")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()

# Observations-Salaries are not uniform,which is not necessarily a discrepancy,bt we do observe that there are employees with salaries on either exterimities of histogram.
# Based on the histogram,we can see that the count of the highest earning employee is very less.


# Task-Subset the data based on thresolds

# Employee with healthy eating greater than 8
sub1 = data[data["healthy_eating"] > 8]
# Employee with salary less than 1000
sub2 = data[data["salary"] < 1000]

# print(sub1)
# print(sub2)

# Employee with healthy eating greater than 8 and salary less than 1000
sub = data[(data["healthy_eating"] > 8) & (data["salary"] < 1000)]
# print(sub)
#Observations-The only employee is present here,and his id is 26 and age is 62

#Final Conclusions-From the given data we can visualize how the given data are distributed,
#we can conduct preliminary analysis by subsetting data sets using well thought out thresolds and conditions