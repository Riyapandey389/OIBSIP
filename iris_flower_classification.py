# -*- coding: utf-8 -*-
"""Iris_flower_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1byTNIy1v7OpsUF8mrhjAzilBf6TdgjOf

## **IRIS FLOWER DATASET CLASSIFICATION**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df= pd.read_csv("/content/Iris.csv")
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

sns.pairplot(df, hue="Species")
plt.show()

# Select only numerical features for correlation calculation
numerical_features = df.select_dtypes(include=np.number)  # Select columns with numerical data types

# Calculate correlation for numerical features only
sns.heatmap(numerical_features.corr(), annot=True, cmap="coolwarm")
plt.show()

X= df.iloc[:, :-1]
y=df.iloc[: , -1]

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)

#k nearest neighbor

knn= KNeighborsClassifier(  n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn= knn.predict(X_test)
print(accuracy_score(y_test,y_pred_knn))

#Support Vector Machine
svm=SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred_svm= svm.predict(X_test)
print(accuracy_score(y_test,y_pred_svm))

#Decision Tree
dt=DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred_dt= dt.predict(X_test)
print(accuracy_score(y_test,y_pred_dt))

#Random Forest
rf=RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf= rf.predict(X_test)
print(accuracy_score(y_test,y_pred_rf))

print(classification_report(y_test, y_pred_rf))
sns.heatmap(confusion_matrix(y_test,y_pred_rf), annot=True, fmt='d', cmap='Blues')
plt.show()

import joblib
# Assign the model you want to save to the variable 'model'
model = rf

joblib.dump(model, "model.pkl")
print(" Model saved as model.pkl ")

pip freeze > requirements.txt