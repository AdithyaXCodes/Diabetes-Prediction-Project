# Exploratory Data Analysis Report

## Introduction
This report provides insights into the data used for training the diabetes prediction models.

## Data Overview
- **Total Records**: 768
- **Missing Values**: 
    - Glucose: 5 missing values replaced with mean.
    - Insulin: 10 missing values replaced with mean.

## Key Findings
- **Feature Distributions**:
    - Glucose levels are positively skewed with a mean of 120.
    - BMI values show a normal distribution centered around 30.

## Correlation Matrix
![Correlation Matrix](images/correlation_matrix.png)

## Conclusion
The analysis indicates significant relationships between certain features (e.g., Glucose and Outcome). These insights will guide feature selection for model training.