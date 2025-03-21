# -*- coding: utf-8 -*-
"""Unemployment_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AnrKbazWCAxjOXASnjtYpGMNi4wxdHrC
"""

#Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import io

#loading dataset and reading it's content

zip_file_path="/content/archive (16) (2).zip"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:

    file_names = zip_ref.namelist()
    with zip_ref.open("Unemployment in India.csv") as csv_file1:
        df_csv1 = pd.read_csv(csv_file1)

    with zip_ref.open("Unemployment_Rate_upto_11_2020.csv") as csv_file2:
        df_csv2 = pd.read_csv(csv_file2)

    display(df_csv1.head())
    display(df_csv2.head())

#Data Preprocessing

print("Missing Value in First Dataset:\n", df_csv1.isnull().sum())
print("Missing Value in Second Dataset:\n", df_csv2.isnull().sum(), df_csv2.isnull().sum())

df_csv1["Date"]=pd.to_datetime(df_csv1["Date"], dayfirst=True)
df_csv2["Date"]=pd.to_datetime(df_csv2["Date"], dayfirst=True)


df_csv1.columns=df_csv1.columns.str.strip(),str.lower(), str.replace(" ", "_")
df_csv2.columns=df_csv2.columns.str.strip(),str.lower(),str.replace(" ", "_")

display("Data types before preprocessing:\n", df_csv1.dtypes)
display("Data types after preprocessing:\n", df_csv2.dtypes)

#Exploratry Dat Analysis

display("Summary Statistics of First dataset:\n", df_csv1.describe())
display("Unique regions:\n", df_csv1["Region"].unique())
display("Unique frequency values:\n", df_csv1[" Frequency"].unique())

display("Summary Statistics of Second dataset:\n", df_csv2.describe())
display("Unique regions:\n", df_csv2["Region"].unique())
display("Unique frequency values:\n", df_csv2[" Frequency"].unique())

"""### Data visualization"""

#Unemployment Rate Trends over Time

plt.figure(figsize=(20, 6))
sns.lineplot(data=df_csv1, x=" Date", y=" Estimated Unemployment Rate (%)", hue="Region") # Changed 'Data' to 'data', 'X' to 'x', and "Region" to "region"
plt.title("Unemployment Rate Over Time By Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title="Region", bbox_to_anchor=(1.05,1), loc="upper left")
plt.show()

#Distribution Of estimated Employed Population

plt.figure(figsize=(20, 4))
sns.histplot(data=df_csv1[" Estimated Employed"],bins=30, kde=True)
plt.title("Distribution of Estimated Employed Population")
plt.xlabel("Estimated Employed")
plt.ylabel("Frequency")
plt.show()

#Unemployment Rate by Region

plt.figure(figsize=(20, 6))
sns.barplot(data=df_csv1, x="Region", y=" Estimated Unemployment Rate (%)")
plt.title("Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.show()

"""#Statistical Analysis

"""

numeric_df = df_csv1.select_dtypes(include=np.number)

# Calculate the correlation matrix
corr_matrix = numeric_df.corr()

# Plotting the heatmap
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Unemployment Data")

#Modelling(Linear Regression)

X = df_csv1[[" Estimated Employed", " Estimated Unemployment Rate (%)"]]
y = df_csv1[" Estimated Unemployment Rate (%)"]

df_cleaned = df_csv1.dropna(subset=[" Estimated Employed", " Estimated Unemployment Rate (%)"])
# Corrected column name to match the name in the DataFrame: ' Estimated Employed'
X= df_cleaned[[" Estimated Employed"]]
y= df_cleaned[[" Estimated Unemployment Rate (%)"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse} ")

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred,color="Green", alpha=0.6)

plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'r',lw=2)

plt.xlabel("Actual Unemployment Rate")
plt.ylabel("Predicted Unemployment Rate")
plt.title("Actual vs Predicted Unemployment Rate")
plt.show()

#Residual Plotting

Residuals =y_test-y_pred
plt.figure(figsize=(8,6))
sns.histplot(Residuals,bins=30,kde=True)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.title("Residual Distribution")
plt.show()

"""# #Final Insights
- The residual are normally distributed ,meaning the model is unbiased
- A scatter plot shows most predictions align closely with actual values
-
Higher unemployment rates tend to have slightly higher prediction errors
"""

import joblib
# Assign the model you want to save to the variable 'model'
model = model  # Changed 'rf' to 'model'

joblib.dump(model, "model.pkl")
print(" Model saved as model.pkl ")

pip freeze > requirements.txt

from google.colab import drive
drive.mount('/content/drive')