# Disease Predictor — Machine Learning + Flask

A simple, lightweight web app that predicts likely diseases from selected symptoms using a trained ML model and serves results via a Flask web interface. The repository contains training/testing CSV files, the Flask app (`app.py`), static assets and templates, and a `Procfile` for easy deployment. Demo (if available) is linked on the repo page. :contentReference[oaicite:0]{index=0}

---

## Demo
Live demo (if running): `https://disease-predictor-1-zp9p.onrender.com` (check repository page for current deployment). :contentReference[oaicite:1]{index=1}

---

## Table of contents
- [About](#about)  
- [Features](#features)  
- [Repository structure](#repository-structure)  
- [Prerequisites](#prerequisites)  
- [Installation & Run (Local)](#installation--run-local)  
- [Train / Update the Model](#train--update-the-model)  
- [Deploy (Render / Heroku / Other)](#deploy-render--heroku--other)  
- [Contributing](#contributing)  
- [License & Contact](#license--contact)

---

## About
This project provides a small web UI where users can select symptoms (up to N items) and receive a model-based suggestion (example: Decision Tree prediction). It is ideal as a learning/demo app showing how to combine data (CSV), a scikit-learn model (or similar), and a Flask frontend to deliver quick predictions.

---

## Features
- Simple Flask-based web UI for symptom selection.  
- Backend prediction endpoint that uses preprocessed CSV datasets (`Training.csv`, `Testing.csv`).  
- Static assets and templates for a modern UI.  
- `Procfile` included for easy deployment (e.g., Render, Heroku).  
- Lightweight — easy to run locally and extend.

(Exact model type and preprocessing are implemented in `app.py` — open that file to see how features are encoded and how predictions are produced.) :contentReference[oaicite:2]{index=2}

---

## Repository structure (important files)
(If your repo differs slightly, treat this as a guideline and inspect the actual files.) :contentReference[oaicite:3]{index=3}

---

## Prerequisites
- Python 3.8+  
- pip (Python package manager)  
- (Optional) virtual environment tool: `venv` or `virtualenv`  
- Git (to clone the repo)

---

## Installation & Run (Local)
1. Clone the repo:
```bash
git clone https://github.com/Sam95344/Disease-Predictor.git
cd Disease-Predictor


2. Create and activate a virtual environment:
python3 -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# or Windows (cmd)
venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4. Run the Flask app (development):
# If app.py exposes 'app' (Flask object):
export FLASK_APP=app.py        # macOS / Linux
set FLASK_APP=app.py           # Windows (cmd)
$env:FLASK_APP = "app.py"      # PowerShell

flask run
# or directly:
python app.py














