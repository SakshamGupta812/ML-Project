# 🎓 Student Performance Prediction

An end-to-end Machine Learning web application that predicts a student's **Math Score** based on demographic information, parental education, lunch type, test preparation, reading score, and writing score.

The project demonstrates the complete Machine Learning workflow — from data preprocessing and model training to Flask deployment, Docker containerization, GitHub Actions CI/CD, Docker Hub, and Render deployment.

## 🚀 Live Demo

🌐 **[Open Student Performance Prediction App](https://studentperformance-app-se4a.onrender.com/)**

> Note: The application is hosted on Render's free instance. If the service has been inactive, the first request may take some time while the instance starts.

---

## 📌 Project Overview

The application takes the following student information as input:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The trained Machine Learning model then predicts the student's **Math Score**.

---

## 🛠️ Technologies Used

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- XGBoost

### Data Preprocessing
- SimpleImputer
- StandardScaler
- OneHotEncoder
- ColumnTransformer

### Web Development
- Flask
- HTML
- CSS

### Deployment & MLOps
- Docker
- GitHub
- GitHub Actions
- Docker Hub
- Render

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Ingestion
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Flask Web Application
   ↓
Docker Container
   ↓
GitHub Actions CI/CD
   ↓
Docker Hub
   ↓
Render Deployment
   ↓
Live Application