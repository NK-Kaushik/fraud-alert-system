# 🏦 AI-Based Fraud Alert Triage & Analyst Explanation System

## 📌 Overview

Banks already detect fraudulent transactions using rules and machine-learning models.
However, the **real operational challenge** is not detection — it is:

* Excessive **false positives**
* **Fraud analyst overload**
* Lack of **clear explanations** for why an alert was raised

This project builds a **decision-support AI system** that helps fraud analysts **prioritize alerts and understand risk**, rather than automatically blocking users.

The system combines:

* Machine-learning–based **fraud risk scoring**
* Business-driven **alert triage**
* Explainable, **compliance-safe analyst explanations**
* A **REST API** for real-world integration

Humans remain **in the loop** at all times.

---

## 🎯 Key Objectives

* Estimate **fraud risk probability**, not hard decisions
* Reduce analyst fatigue through **risk-based prioritization**
* Provide **clear, audit-friendly explanations**
* Follow **real banking workflows and compliance expectations**
* Design the system as a **production-style service**, not a notebook

---

## 🧠 System Architecture

```
Incoming Transaction
        ↓
Fraud Risk Model (PyTorch)
        ↓
Alert Triage Logic
        ↓
Explanation Layer
        ↓
REST API Response
```

Each layer is intentionally separated to ensure:

* Auditability
* Maintainability
* Regulatory safety
* Scalability

---

## 🛠️ Tech Stack

| Layer           | Technology                     |
| --------------- | ------------------------------ |
| Language        | Python                         |
| ML Model        | PyTorch (Neural Network / MLP) |
| Data Processing | Pandas, NumPy, scikit-learn    |
| Explainability  | Rule-based (LLM-ready design)  |
| API             | FastAPI                        |
| Serving         | Uvicorn                        |
| Environment     | Python virtual environment     |

---

## 📁 Project Structure

```
fraud-alert-system/
├── api/
│   └── main.py
├── data/
│   ├── load_data.py
│   └── prepare_features.py
├── model/
│   └── train_model.py
├── triage/
│   └── risk_prioritizer.py
├── explainability/
│   └── llm_explainer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Project

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start API
uvicorn api.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Dataset

* Public credit-card fraud transaction dataset
* Highly imbalanced (≈0.17% fraud)
* Anonymized features (PCA-based)

📌 **Note:**
The dataset is **not committed** to the repository due to size and industry best practices.
Users are instructed to download it separately and place it in `data/transactions.csv`.

---

# 🔍 Step-by-Step Implementation (What I Did, Why I Did It, and How It’s Used)

This section explains the **engineering and ML decisions step by step**.

---

## ✅ Step 1 — Project & Git Setup

### What I did

* Created a clean, modular repository structure
* Initialized Git and configured `.gitignore`
* Excluded large data files, models, and environments

### Why I did it

* Mirrors how ML projects are structured in real companies
* Keeps the repository lightweight and reproducible
* Prevents committing machine-specific or sensitive artifacts

### How it’s used

* Enables easy onboarding for reviewers
* Supports clean version control and collaboration

---

## ✅ Step 2 — Virtual Environment & Dependency Isolation

### What I did

* Created and activated a Python virtual environment
* Defined dependencies explicitly in `requirements.txt`

### Why I did it

* Prevents dependency conflicts across projects
* Ensures consistent runtime behavior across machines
* Required for reproducible ML workflows

### How it’s used

* All packages are installed in an isolated environment
* Anyone can recreate the setup using `pip install -r requirements.txt`

---

## ✅ Step 3 — Dataset Ingestion & Problem Framing

### What I did

* Loaded the fraud dataset using Pandas
* Analyzed class imbalance
* Framed the task as **risk estimation**, not classification

### Why I did it

* Fraud datasets are extremely imbalanced
* Accuracy alone is misleading in this domain
* Banks care about **prioritization**, not binary decisions

### How it’s used

* Guides model design
* Drives the need for triage and human review

---

## ✅ Step 4 — Feature Preparation & Train/Test Split

### What I did

* Separated features and labels
* Applied **standardization**
* Used **stratified train-test split**

### Why I did it

* Neural networks are sensitive to feature scale
* Stratification preserves rare fraud distribution
* Prevents misleading evaluation

### How it’s used

* Produces PyTorch-ready tensors
* Ensures fair and realistic model training

---

## ✅ Step 5 — Fraud Risk Model Training (PyTorch)

### What I did

* Built a feed-forward neural network (MLP)
* Trained using **class-weighted loss**
* Saved the model for inference

### Why I did it

* Fraud is rare → misclassification cost is asymmetric
* Class-weighted loss penalizes missed fraud more heavily
* Simple architectures are preferred in regulated domains

### How it’s used

* Outputs a **fraud probability**
* Serves as an advisory signal, not a final decision

---

## ✅ Step 6 — Alert Triage & Prioritization Logic

### What I did

* Converted risk scores into **HIGH / MEDIUM / LOW** priority
* Incorporated business signals (amount, velocity, geography)

### Why I did it

* Analysts work top-down by urgency
* Reduces false positives and alert fatigue
* Separates ML from business decisions

### How it’s used

* Determines which alerts analysts see first
* Preserves human control over final actions

---

## ✅ Step 7 — Explanation Layer (LLM-Ready Design)

### What I did

* Generated analyst-friendly explanations
* Used compliance-safe, non-definitive language
* Kept logic deterministic and auditable

### Why I did it

* Analysts need context, not just scores
* Explanations must be reviewable and consistent
* LLMs should assist, not decide

### How it’s used

* Improves analyst efficiency
* Supports regulatory review and audit trails

---

## ✅ Step 8 — REST API Integration (FastAPI)

### What I did

* Built a REST API to orchestrate all components
* Exposed `/analyze-transaction` endpoint
* Returned structured JSON output

### Why I did it

* Real systems consume ML via APIs
* Enables integration with monitoring systems and dashboards
* Demonstrates production-thinking

### How it’s used

* Analysts or downstream systems can request risk assessments
* Makes the project demo-ready and scalable

---

## 🧠 Key ML Concepts Used

* Supervised learning
* Neural networks (MLP)
* Class imbalance handling
* Feature standardization
* Stratified sampling
* Probability-based risk scoring
* Threshold-based decisioning
* Human-in-the-loop AI design

---



## 📜 License

MIT License
