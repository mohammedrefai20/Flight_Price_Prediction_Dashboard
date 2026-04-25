# ✈️ Flight Price Prediction Dashboard

> An interactive analytics dashboard built with **Plotly Dash** and a **Random Forest / Gradient Boosting** machine learning model to explore and predict Indian domestic flight prices.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-4.0-008DE4?style=flat&logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.5-3F4F75?style=flat&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.1-150458?style=flat&logo=pandas&logoColor=white)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Dashboard Features](#-dashboard-features)
- [Machine Learning Model](#-machine-learning-model)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)

---

## 🔍 Overview

This project is a **university data visualization project** that combines exploratory data analysis (EDA) with a machine learning price predictor — all inside a single interactive Dash dashboard.

The dashboard has **two main sections:**

| Section | Description |
|---------|-------------|
| **Part 1 — EDA & Insights** | KPI cards, interactive charts with live sidebar filters |
| **Part 2 — Price Prediction** | Input form → ML model → predicted price + feature importance |

---

## 📦 Dataset

**Source:** [Kaggle — Flight Price Prediction](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

| Property | Value |
|----------|-------|
| Rows | 300,153 |
| Features | 11 |
| Target | `price` (INR) |

### Features

| Column | Type | Description |
|--------|------|-------------|
| `airline` | categorical | Name of the airline |
| `source_city` | categorical | City of departure |
| `destination_city` | categorical | City of arrival |
| `departure_time` | categorical | Time slot of departure (Morning, Evening, etc.) |
| `arrival_time` | categorical | Time slot of arrival |
| `stops` | categorical | Number of stops (zero, one, two or more) |
| `class` | categorical | Economy or Business |
| `duration` | float | Flight duration in hours |
| `days_left` | int | Days between booking and departure |
| `price` | int | Ticket price in INR (**target variable**) |

---

## 🗂️ Project Structure

```
Flight_Price_Prediction_Dashboard/
│
├── 📄 app.py                        ← Entry point (Gunicorn-compatible)
├── 📄 main.py                       ← App initialization and server setup
├── 📄 preprocessor.py               ← Data loading and cleaning class
├── 📄 visuals.py                    ← All Plotly chart functions
├── 📄 model.py                      ← ML training, prediction, evaluation
├── 📄 layout.py                     ← Full Dash UI layout and callbacks
│
├── 📊 Flight Price Prediction.csv   ← Raw dataset
├── 🤖 model.pkl                     ← Trained model (saved after running model.py)
└── 📋 requirements.txt              ← Python dependencies
```

### File responsibilities

```
preprocessor.py  →  loads CSV, drops unused columns, fixes duration format
      ↓
   model.py       →  encodes features, trains model, saves model.pkl
      ↓
  visuals.py      →  pure chart functions (no Dash, just Plotly figures)
      ↓
  layout.py       →  Dash layout + all callbacks (wires filters to charts)
      ↓
   main.py        →  creates Dash app, loads data + model, registers layout
      ↓
    app.py        →  exposes `server` for production, calls app.run() locally
```

---

## 📊 Dashboard Features

### Part 1 — EDA & Insights

#### KPI Cards
Five summary statistics displayed at the top of the dashboard:

- 💰 **Average Price** (INR)
- 🪑 **Economy Tickets** count
- 💼 **Business Tickets** count
- ⏱️ **Average Duration** (hours)
- ✈️ **Number of Airlines**

#### Interactive Charts

| Chart | Type | Description |
|-------|------|-------------|
| Average price by airline | Bar chart | Sorted by price descending with value labels |
| Economy vs Business share | Pie chart | Ticket count split by travel class |
| Source → Destination pricing | Heatmap | Average price for every city pair |
| Price by number of stops | Box plot | Distribution and outliers per stop category |
| Average duration by airline | Horizontal bar | Mean flight time per carrier |
| Price trend vs days left | Line chart | How price changes as departure approaches |

#### Sidebar Filters
All 6 charts update **simultaneously** when you change any filter:

- Airline (multi-select dropdown)
- Class (multi-select dropdown)
- Source city (multi-select dropdown)
- Destination city (multi-select dropdown)
- Stops (multi-select dropdown)
- Max price (slider)

---

### Part 2 — ML Price Prediction

#### Input Form
Users fill in 8 fields to describe their flight:

- Airline, Class, Source city, Destination city
- Departure time, Arrival time, Stops
- Duration (slider in hours), Days before flight (number input)

#### Output
- **Predicted price** displayed instantly in INR
- **Feature importance chart** always visible — shows which factors affect price most

---

## 🤖 Machine Learning Model

### Pipeline

```
Raw data
   ↓
FlightPreprocessor          — drops unused columns, converts duration to HH:MM
   ↓
prepare_features()          — LabelEncoder for 7 categorical columns
   ↓
train_test_split()          — 80% train / 20% test, random_state=42
   ↓
GradientBoostingRegressor   — 50 trees, max_depth=5, learning_rate=0.1
   ↓
Evaluation                  — MAE, RMSE, R²
   ↓
model.pkl                   — saved bundle: model + encoders + feature names + metrics
```

### Model Performance

| Metric | Value |
|--------|-------|
| **R²** | 0.9792 |
| **MAE** | ~1,687 INR |
| **RMSE** | ~3,278 INR |

### Why these features matter

Based on feature importance, the top predictors of flight price are:

1. `class` — Business tickets cost significantly more than Economy
2. `days_left` — Prices rise sharply as departure approaches
3. `duration` — Longer flights generally cost more
4. `stops` — Direct flights vs connecting flights affect price
5. `airline` — Carrier premium varies widely

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/flight-price-dashboard.git
cd flight-price-dashboard
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` contents:

```
dash==4.0.0
plotly==6.5.2
pandas==2.1.4
numpy==1.26.4
scikit-learn==1.8.0
gunicorn==25.3.0
```

### 4. Download the dataset

Download `Flight Price Prediction.csv` from [Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) and place it in the project root folder.

---

## ▶️ How to Run

### Step 1 — Train the model

Run this **once** to generate `model.pkl`:

```bash
python model.py
```

Expected output:
```
Preparing features ...
Train rows : 240,122  |  Test rows : 60,031
Training Gradient Boosting ...
  MAE  : 1,687 INR
  RMSE : 3,278 INR
  R²   : 0.9792
Model saved to model.pkl
```

### Step 2 — Start the dashboard

```bash
python app.py
```

Expected output:
```
Loading data ...
  Rows loaded : 300,153
Loading model ...
  R² : 0.9792
Dash is running on http://127.0.0.1:8050/
```

### Step 3 — Open in browser

Go to **http://127.0.0.1:8050**

> Press `Ctrl + C` in the terminal to stop the server.

---

## 🖼️ Screenshots

> Add screenshots of your running dashboard here.

```
dashboard-overview.png     ← Part 1: KPI cards + charts
prediction-panel.png       ← Part 2: prediction form + result
sidebar-filters.png        ← Sidebar with active filters
```

*To add screenshots: take a screenshot of your running dashboard, save it in a `/screenshots` folder, and reference it here with:*

```markdown
![Dashboard Overview](screenshots/dashboard-overview.png)
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| [Python](https://python.org) | 3.11 | Core language |
| [Dash](https://dash.plotly.com) | 4.0 | Web dashboard framework |
| [Plotly](https://plotly.com) | 6.5 | Interactive charts |
| [Pandas](https://pandas.pydata.org) | 2.1 | Data manipulation |
| [NumPy](https://numpy.org) | 1.26 | Numerical operations |
| [scikit-learn](https://scikit-learn.org) | 1.8 | Machine learning model |
| [Gunicorn](https://gunicorn.org) | 25.3 | Production WSGI server |

---

## 👤 Author

**Mohammed Refai**
ITI — AI Track
Data Exploration and Visualization Project

---

## 📄 License

This project is for educational purposes as part of the ITI AI program.
