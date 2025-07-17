# 🔥 Calories Burnt Prediction using Machine Learning

## 📌 Project Overview
This project aims to predict the number of **calories burnt** based on various physical activity and body-related features using **Machine Learning regression models**.  
Calorie prediction is essential for fitness tracking applications and helps individuals manage weight and health goals effectively.

---

## ✅ Problem Statement
Given features like **age**, **weight**, **height**, **duration of exercise**, and **heart rate**, the goal is to build a model that accurately predicts **calories burnt**.

---

## 🛠 Steps Taken:
### 1️⃣ **Data Collection & Understanding**
- Loaded and inspected the dataset containing fitness-related features.
- Checked for missing values and incorrect data types.

### 2️⃣ **Data Cleaning & Preprocessing**
- Removed duplicates and handled missing values.
- Scaled numerical data for better model accuracy.

### 3️⃣ **Exploratory Data Analysis (EDA)**
- Analyzed distributions of key features.
- Visualized correlations between **heart rate**, **duration**, and calories burnt.

### 4️⃣ **Feature Engineering**
- Selected top features influencing calorie burn:
  - Duration
  - Heart Rate
  - Body Weight
  - Age

### 5️⃣ **Model Building**
- Applied multiple regression models:
  - **Linear Regression**
  - **Random Forest Regressor**
  - **Gradient Boosting**
- Evaluated models using:
  - **R² Score**
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**

### 6️⃣ **Model Evaluation**
- Compared performance and selected the most accurate model.

---

## 📈 Key Insights:
✔ Longer duration and higher heart rate significantly increase calorie burn.  
✔ Random Forest and Gradient Boosting models provide the best accuracy.

---

## 🛠 Tools & Technologies:
- **Python**
- **Libraries**: `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Scikit-learn`
- **Jupyter Notebook** for model development.

---

## 📂 Project Structure
