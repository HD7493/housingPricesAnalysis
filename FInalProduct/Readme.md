# House Price Prediction

## Introduction
Welcome to our exciting journey into the heart of the Greater Toronto Area's real estate landscape! Our project aims to develop a tool that empowers homebuyers, investors, and dreamers with the knowledge needed to make confident decisions in the dynamic GTA real estate market.

## Mission
Our mission is to develop a machine-learning model that predicts house prices with uncanny accuracy. Beyond numbers and algorithms, we aim to demystify the real estate process and guide you on your journey to finding your perfect place in the world.

## Business Problem
Our project addresses the challenge of accurate house price prediction in the Greater Toronto Area (GTA). We aim to develop a machine-learning model that provides reliable insights into housing trends, empowering stakeholders to make informed decisions.

## Client
Our primary clients are stakeholders in the GTA real estate industry, including agencies, developers, investors, and individual buyers and sellers. By providing a predictive model tailored to their needs, we seek to enhance their ability to understand market dynamics and identify investment opportunities.

## Objective
Our project aims to gain insights into the factors influencing house prices in the GTA and develop a machine-learning model capable of accurately predicting prices based on these factors. By achieving these objectives, we aim to empower stakeholders with actionable insights for effective decision-making.

## Obtaining the Data
We encountered challenges in obtaining comprehensive real estate data from the Toronto Regional Real Estate Board (TRREB) due to data access limitations and format constraints. We developed a systematic approach to extract and convert the data into a more accessible format for analysis.

## Cleaning The Data
After obtaining the raw data, we cleaned it by handling null values, treating outliers, ensuring data consistency, and performing feature engineering tasks.

## Exploratory Data Analysis (EDA)
We conducted comprehensive EDA to understand the dataset's nuances, including univariate and bivariate analyses for categorical and numerical variables.

## Base Model Evaluation
We built a base model using the Random Forest Regressor and evaluated its performance using metrics such as Mean Squared Error (MSE), R-squared, Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

## Feature Importance
We calculated the feature importance of the model to understand which features contribute most to predicting the target variable (Sold Price).

## Data Encoding
Categorical variables were encoded using techniques such as one-hot encoding, label encoding, and frequency encoding.

## Feature Importance & Performance Matrix After Data Encoding
We re-evaluated the model after data encoding to assess its impact on performance and feature importance.

## Scaling Data
Numerical variables were standardized using standard scaling and min-max scaling techniques.

## Model Comparison Using Lazy Predict Regressor
We compared multiple regression models using the LazyRegressor library to select the best-performing model for predicting housing prices.

## Individual Model Building and Evaluation
Several individual regression models were built and evaluated, with the LightGBM Regressor emerging as the top-performing model.

## Model Deployment
We deployed the LightGBM Regressor model in a web application developed using Django, providing users with a user-friendly interface for predicting housing prices.

## Future Scope
Our future scope includes nationwide expansion, mobile optimization, community engagement, and partnerships to enhance the predictive models.

## Summary
The project successfully delivered an accurate housing price prediction tool while setting the stage for broader applications and improvements.

## References
- TRREB - [Home](https://www.trreb.ca/)
- Online Image-To-Excel converter tool - [extracttable](https://www.extracttable.com/)
