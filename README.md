# ADS-B Spoofing Detection System

## Overview
This project implements a machine learning-based system to detect potential spoofing in ADS-B (Automatic Dependent Surveillance–Broadcast) signals. It identifies abnormal aircraft behavior using derived motion features and visualizes results through an interactive web interface.

## Problem Statement
ADS-B systems broadcast aircraft position and velocity without encryption, making them vulnerable to spoofing attacks. This project focuses on detecting such anomalies using data-driven techniques.

## Approach
The system performs:

- Data preprocessing and cleaning
- Feature engineering using temporal differences:
  - Latitude change
  - Longitude change
  - Altitude variation
  - Velocity anomalies
- Rule-based labeling for anomaly detection
- Machine learning classification using Random Forest

## System Architecture
1. Raw ADS-B data is processed to extract meaningful features  
2. Features are used to train a classification model  
3. A Streamlit-based interface allows:
   - User input testing
   - Visualization of aircraft movement
   - Detection of spoofed signals  

## Features
- Interactive map visualization of aircraft positions  
- Real-time prediction using trained ML model  
- Lightweight and deployable web application  
- Clean separation of UI (`app.py`) and logic (`core.py`)  

## Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Plotly  

## Model Details
- Algorithm: Random Forest Classifier  
- Input Features:
  - Latitude, Longitude
  - Velocity
  - Altitude
  - Derived difference features  
- Output:
  - Normal Signal  
  - Spoofed Signal  

## Project Structure
app.py
core.py
model.pkl
features.pkl
requirements.txt
.gitignore

## Deployment
The application is deployed using Streamlit Cloud.

## Limitations
- Uses rule-based labeling (not real-world labeled spoof data)  
- No real-time ADS-B feed integration  
- Model performance depends on feature thresholds  

## Future Work
- Integration with live ADS-B streams  
- Use of advanced anomaly detection models  
- Improved feature engineering with time-series methods  

## Author
Zuha Jagirdar
