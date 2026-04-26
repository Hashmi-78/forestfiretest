# 🌲🔥 Algerian Forest Fire Prediction

A Machine Learning web application that predicts the **Fire Weather Index (FWI)** based on environmental parameters. Built with Flask and deployed on AWS Elastic Beanstalk with a CI/CD pipeline connected to GitHub.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![AWS](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-orange.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-red.svg)

---

## 🌐 Live Demo
🔗 [Forestfiretest-env.eba-56sbq2y8.eu-north-1.elasticbeanstalk.com](http://Forestfiretest-env.eba-56sbq2y8.eu-north-1.elasticbeanstalk.com)

---

## 📌 About the Project

This project uses the **Algerian Forest Fires Dataset** to predict the Fire Weather Index (FWI) — a key indicator of fire danger. The model is trained using **Ridge Regression** and deployed as a web app where users can input environmental conditions and get an instant FWI prediction.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Framework | Flask |
| ML Model | Ridge Regression (Scikit-learn) |
| Web Server | Gunicorn + Nginx |
| Hosting | AWS Elastic Beanstalk |
| CI/CD | AWS CodePipeline + GitHub |
| Version Control | Git & GitHub |

---

## 📊 Input Features

| Feature | Description |
|---|---|
| Temperature | Ambient temperature in °C |
| RH | Relative Humidity (%) |
| Ws | Wind Speed (km/h) |
| Rain | Rainfall in mm |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire/No Fire (0 or 1) |
| Region | Bejaia (0) or Sidi-Bel Abbes (1) |

---

## 🚀 Deployment Architecture

```
GitHub (main branch)
        ↓
AWS CodePipeline (auto-triggered on push)
        ↓
AWS Elastic Beanstalk (Python 3.14 on Amazon Linux 2023)
        ↓
Nginx + Gunicorn → Flask App
        ↓
Live Web App 🌐
```

---

## 💻 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Hashmi-78/forestfiretest.git
cd forestfiretest
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python application.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 📁 Project Structure

```
forestfiretest/
├── .ebextensions/
│   └── python.config        # AWS EB configuration
├── models/
│   ├── ridge.pkl            # Trained Ridge Regression model
│   └── scaler.pkl           # Standard Scaler
├── templates/
│   └── home.html            # Prediction form UI
├── application.py           # Flask app
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📷 Screenshots

> ![alt text](<Empty form.png>)
![alt text](<result form.png>)
---

## 🧠 Model Details

- **Algorithm:** Ridge Regression
- **Dataset:** Algerian Forest Fires Dataset (UCI ML Repository)
- **Target Variable:** FWI (Fire Weather Index)
- **Preprocessing:** Standard Scaler for feature normalization

---

## ⚠️ Challenges Faced

- Configuring `.ebextensions/python.config` with correct YAML formatting
- Setting up IAM roles for CodePipeline and Elastic Beanstalk
- Fixing 502 Bad Gateway errors with Gunicorn/Nginx configuration
- Structuring the GitHub repo correctly for EB deployment

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author
**Umar Hashmi**
- GitHub: [@Hashmi-78](https://github.com/Hashmi-78)
- LinkedIn: www.linkedin.com/in/muhammad-umar-usman-hashmi-4a34002b8

---

⭐ If you found this project helpful, please give it a star!
