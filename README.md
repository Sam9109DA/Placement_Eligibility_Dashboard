# 📊 Placement Eligibility Dashboard

A data-driven dashboard built using **Python, Streamlit, and MySQL** to analyze student performance and evaluate placement readiness.

---

## 🚀 Overview

This project helps identify which students are ready for placements based on key metrics like:

- CodeKata Score
- Career Track Performance
- Soft Skills (Communication & Teamwork)
- Placement Status Trends

It provides **interactive filtering, real-time insights, and visual analytics** to support decision-making.

---

## 🧠 Key Insights

- Not all high scorers get placed → Technical skills alone are not enough
- Career Track & Soft Skills influence placement outcomes
- Placement distribution helps identify overall readiness gap
- Performance comparison highlights real-world patterns

---

## ⚙️ Features

- 🎯 Filter students by CodeKata & Career Track scores
- 📈 Eligibility percentage calculation
- 🧮 Average performance metrics
- 🏆 Top students ranking
- 📊 Placement status distribution
- 🔍 Search students by name
- 📥 Download results as CSV
- 📉 Score distribution visualization

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **MySQL**
- **SQL (Aggregations, Joins, Group By)**
- **Faker** 

## 🧠 Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Data Analysis & Visualization
- Dashboard Development
- SQL Query Optimization

---

## 📸 Screenshots

### 🏠 Dashboard Overview
![Dashboard]!(<Dashboard (2)-1.png>)

### 📊 Insights Panel
![Insights]!(<Insights-1.png>)

### 📈 Performance Charts
![Chart 1]!(<Chart 1-1.png>)
![Chart 2]!(<Chart 2-1.png>)

### 🏆 Top Students Output
![Results]!(<Result-1.png>)

---
## ⚙️ Database Setup

This project uses **SQLite** for deployment compatibility.

- Originally designed with MySQL
- Migrated to SQLite for Streamlit Cloud hosting

Run the following to initialize database:

```bash
python init_db.py


## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Sam9109DA/Placement_Eligibility_Dashboard.git
cd Placement_Eligibility_Dashboard