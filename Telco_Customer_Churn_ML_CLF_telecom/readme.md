# Telco Customer Churn

# Objective

This repository contains code and resources for predicting customer churn in a telecom company (Telco). The goal of this project is to develop a machine learning model that can accurately predict whether a customer is likely to churn (leave) the telecom service provider based on various features.

# Data Information
Dataset Characteristics: Binary Classification

Subject Area: Telecom

Associated Tasks: Classification

Feature Type: Real

Instances: 5785

# Data Dictionary
- **customerID** : Customer ID
- **gender** : Whether the customer is a male or a female
- **SeniorCitizen** : Whether the customer is a senior citizen or not (1, 0)
- **Partner** : Whether the customer has a partner or not (Yes, No)
- **Dependents** : Whether the customer has dependents or not (Yes, No)
- **tenure** : Number of months the customer has stayed with the company
- **PhoneService** : Whether the customer has a phone service or not (Yes, No)
- **MultipleLines** : Whether the customer has multiple lines or not (Yes, No, No phone service)
- **InternetService** : Customer’s internet service provider (DSL, Fiber optic, No)
- **OnlineSecurity** : Whether the customer has online security or not (Yes, No, No internet service)
- **OnlineBackup** : Whether the customer has online backup or not (Yes, No, No internet service)
- **DeviceProtection** : Whether the customer has device protection or not (Yes, No, No internet service)
- **TechSupport** : Whether the customer has tech support or not (Yes, No, No internet service)
- **StreamingTV** : Whether the customer has streaming TV or not (Yes, No, No internet service)
- **StreamingMovies** : Whether the customer has streaming movies or not (Yes, No, No internet service)
- **Contract** : The contract term of the customer (Month-to-month, One year, Two year)
- **PaperlessBilling** : Whether the customer has paperless billing or not (Yes, No)
- **PaymentMethod** : The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
- **MonthlyCharges** : The amount charged to the customer monthly
- **TotalCharges** : The total amount charged to the customer
- **Churn** : Whether the customer churned or not (Yes or No)

## Overview

The Customer Churn Prediction project focuses on developing a machine learning model to predict customer churn in a telecom company (Telco). Customer churn, or the loss of customers, is a critical concern for telecom companies as it impacts revenue and customer satisfaction. By accurately predicting which customers are likely to churn, the company can take proactive measures to retain them and improve overall customer retention strategies. The project involves data analysis, machine learning model development, and evaluation using various metrics such as accuracy, precision, recall, and F1-score. Through feature engineering and model deployment, the project aims to provide actionable insights to reduce customer churn and enhance customer satisfaction in the telecom industry.

## Project Highlights

1. **Customer Churn Prediction**: This project is centered around forecasting customer churn within a telecommunications company (Telco). Anticipating customer churn is vital for telecom firms to mitigate customer attrition and refine their customer retention strategies.

2. **Machine Learning Model**: The project entails constructing and deploying a machine learning model capable of accurately predicting whether a customer is inclined to churn. This model leverages a variety of features including demographics, usage patterns, and customer behavior to make predictions.

3. **Model Evaluation**: The project includes a thorough evaluation of the predictive model using a range of metrics such as accuracy, precision, recall, and F1-score. Furthermore, ROC curves and AUC are utilized to gauge the model's efficacy in forecasting customer churn.

4. **Data Analysis**: The project involves an in-depth analysis of the Telco customer churn dataset to uncover patterns and insights that can enhance the predictive model. Exploratory data analysis (EDA) techniques are employed to gain insights into the underlying characteristics of the dataset.

## Key Skills Applied

- Data Analysis and Exploration
- Machine Learning Algorithm
- Model Evaluation and Metrics
- Feature Engineering
- Data Preprocessing
- Data-driven Decision Making


# Outcome/Results

|Sr. No.|ML Algorithm|Cross Validation Score|ROC AUC Score|F1 Score (Churn)|
|-|-|-|-|-|
|1|XGBClassifier|84.86%|70.43%|88%|
|2|LightGBMClassifier|84.82%|70.62%|88%|
|3|RandomForestClassifier|82.51%|66.79%|86%|
|4|DecisionTreeClassifier|82.09%|64.52%|87%|
|5|SupportVectorClassifier|80.87%|66.89%|86%|
|6|LogisticRegression|84.46%|70.23%|87%|
|7|Stack of All 6 Classifiers|84.42%|72.13%|88%|


# Further scope of study - NA

