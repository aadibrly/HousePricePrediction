# 🏡 House Price Estimator

An interactive end-to-end Machine Learning web application built using **Python**, **Scikit-Learn**, and **Streamlit**. The app predicts estimated house prices based on key housing and neighborhood metrics using a trained regression model.

---

## 📑 Project Overview
- **Objective:** Provide quick, real-time property value estimations using custom inputs.
- **Model:** Trained using Scikit-Learn's `RandomForestRegressor` pipeline.
- **Frontend:** Clean, responsive UI customized using native Streamlit configuration (`.streamlit/config.toml`).

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data & ML:** Pandas, NumPy, Scikit-Learn
- **Model Persistence:** Pickle
- **Web Interface:** Streamlit

---

## 📦 Repository Structure
```text
house-price-estimator/
├── .streamlit/
│   └── config.toml      # Theme & UI styling settings
├── .gitignore           # File exclusion list
├── app.py               # Streamlit application entry point
├── train_model.py       # Model training & serialization script
├── model.pkl            # Pre-trained ML model binary
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation