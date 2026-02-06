# 🚖 Dynamic Ride Price Predictor

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![ML](https://img.shields.io/badge/Model-Random%20Forest-orange)
![Frontend](https://img.shields.io/badge/UI-Tailwind%20CSS-purple)

A Machine Learning web application that predicts the estimated fare for ride-sharing services (like Uber and Lyft) based on real-time factors like distance, weather, and surge multipliers.

---

## 🌟 Project Overview

This project was developed to understand the mechanics of **Dynamic Pricing**. By analyzing a dataset of Uber and Lyft rides in Boston, I built a system that simulates how prices fluctuate based on demand and environmental conditions.

**Key Features:**
- **Dynamic Inputs:** Users can select Source, Destination, Cab Type, and Service Name.
- **Real-Time Simulation:** Accepts inputs for Distance, Surge Multiplier, and Weather (Temperature, Rain, Humidity).
- **Smart Backend:** Automatically captures the current Hour, Day, and Month to ensure accurate time-based predictions.
- **Interactive UI:** A high-end, 3D-interactive frontend built with Glassmorphism and Tailwind CSS.

---

## 🧠 Model Evolution

I experimented with multiple algorithms to achieve the highest accuracy.

| Model | Status | Performance | Verdict |
| :--- | :--- | :--- | :--- |
| **Linear Regression** |  Initial Attempt | Moderate Accuracy | Good for simple correlations but failed to capture complex pricing surges. |
| **Random Forest** | **Final Model** | **High Accuracy (~96%)** | Excellent at handling non-linear data (like sudden price jumps due to rain or demand). |

**Why Random Forest?**
Ride pricing is non-linear. A simple 2-mile trip might cost $10 normally, but $40 during a rainstorm. Random Forest handles these "decision trees" much better than simple linear equations.

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Data Processing:** Pandas & NumPy
* **Backend Framework:** Flask
* **Frontend:** HTML5, CSS3, Tailwind CSS
* **Serialization:** Joblib (for saving the model)

---

## 📂 Project Structure

Ensure your folder looks exactly like this for the code to run:

```text
ride_project/
│
├── app.py                      # The main Flask Python script
├── Random_Forest_model.joblib   # The trained AI Model
├── encoder.joblib              # OneHotEncoder for categorical data
├── scaler.joblib               # StandardScaler for numerical data
├── README.md                   # This file
│
└── templates/                  # Folder for HTML
    └── index.html              # The Frontend UI