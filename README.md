# 📊 LLM-Based Auto Insight Generator

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20API-orange.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-13.55.78.154-brightgreen.svg)](http://13.55.78.154)

An end-to-end automated **Exploratory Data Analysis (EDA)** web application. Upload any structured CSV dataset to instantly generate statistical profiles, domain-tailored visualizations, and natural-language analytical insights powered by high-speed Large Language Models (LLMs).

---

## 🚀 Key Features

- **Automated Data Profiling & Cleaning**: Automatically cleans datasets by removing empty columns and imputing missing numeric values (mean) and categorical values (mode).
- **Intelligent Chart Selection**: Dynamically selects the best visualizations based on column types and distributions:
  - **Numerical**: Histograms with Kernel Density Estimates (KDE), Box Plots (outlier detection).
  - **Categorical**: Frequency Bar Charts and Distribution Pie Charts for top categories.
  - **Multivariate**: Feature-to-feature Scatter Plots and full Correlation Matrix Heatmaps.
- **AI-Powered Insights**: Integrates with the **Groq API** (`qwen/qwen3.8-27b`) to generate clear, executive-ready narrative explanations for every chart.
- **High-Performance Concurrent Inference**: Utilizes Python's `ThreadPoolExecutor` to query LLM insights in parallel, returning complete analysis dashboards in seconds.
- **Modern Responsive Dashboard**: Interactive single-page web UI with live upload progress spinners, error banners, and cache-busting image rendering.
- **Production-Ready Deployment**: Configured for deployment on AWS Lightsail using Gunicorn WSGI, Nginx reverse proxy, and Systemd process supervision.

---

## 🛠️ Architecture & Pipeline Workflow

```
[ User Uploads CSV ]
        │
        ▼
[ Data Cleaning & Profiling ] ──> Imputes missing values, detects column types
        │
        ▼
[ Chart Selector ] ─────────────> Determines optimal plots (Histograms, Heatmaps, etc.)
        │
        ▼
[ Visualization Engine ] ───────> Matplotlib & Seaborn render charts to PNG
        │
        ▼
[ LLM Inference Engine ] ───────> Concurrent calls to Groq API (Qwen 3.8 / LLaMA)
        │
        ▼
[ Web Dashboard ] ──────────────> Visual cards with charts & contextual AI insights
```

---

## 📂 Project Structure

```
llm-auto-insight-generator/
├── backend/
│   ├── app.py                     # Flask application & route controllers
│   ├── pipeline.py                # Pipeline orchestrator & concurrent worker
│   ├── chart_selector.py          # Intelligent chart type rule engine
│   └── statistics_generator.py    # Statistical computations (mean, median, etc.)
├── llm/
│   ├── llm_client.py              # Groq API client with fallbacks & timeouts
│   └── prompt_builder.py          # Structured prompt engineering for data analysis
├── visualization/
│   ├── chart_generator.py         # Matplotlib & Seaborn plotting routines
│   └── outputs/                   # Directory where generated charts are served
├── utils/
│   ├── basic_cleaning.py          # Missing value handling & cleaning utilities
│   └── data_profiling.py          # Dataset schema and statistics logger
├── templates/
│   └── index.html                 # Clean, responsive HTML5 dashboard
├── static/
│   ├── script.js                  # Frontend upload logic & async UI updates
│   └── style.css                  # Modern UI styles, cards & animations
├── data/                          # Sample datasets for instant testing
│   ├── glass.csv                  # Glass Identification dataset (~200 rows)
│   ├── sample_data.csv            # Real Estate dataset (~13,000 rows)
│   └── Zomato Restaurant Dataset 2.csv
├── .env.example                   # Template for environment configuration
├── requirements.txt               # Production Python dependencies
└── README.md                      # Project documentation
```

---

## ⚡ Quickstart & Local Setup

### 1. Prerequisites
- Python 3.10+ installed
- Free [Groq API Key](https://console.groq.com/)

### 2. Clone Repository
```bash
git clone https://github.com/Nainzee/AI-Dataset-Insight-Generator.git
cd AI-Dataset-Insight-Generator
```

### 3. Create Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Key
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```
Open `.env` and add your Groq API key:
```env
API_KEY="gsk_your_actual_groq_api_key_here"
```

### 6. Run the Application
```bash
python -m backend.app
```
Open your browser and navigate to **[http://localhost:5000](http://localhost:5000)**.

---

## 🌐 Cloud Deployment (AWS Lightsail / EC2)

The application is deployed live with a production stack:
- **Server**: AWS Lightsail Ubuntu 24.04 LTS
- **WSGI Application Server**: Gunicorn (`gthread` worker model)
- **Reverse Proxy**: Nginx on Port 80 with 50MB body size allowance
- **Process Manager**: Systemd (`llm-insights.service`)
- **Virtual Memory**: 2GB swap space for stable data processing

### Systemd Service Configuration
`/etc/systemd/system/llm-insights.service`
```ini
[Unit]
Description=LLM Auto Insight Generator Service
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/llm-auto-insight-generator
Environment="PATH=/home/ubuntu/llm-auto-insight-generator/venv/bin"
ExecStart=/home/ubuntu/llm-auto-insight-generator/venv/bin/gunicorn --workers 2 --threads 2 --timeout 120 --bind 127.0.0.1:5000 backend.app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 🧪 Sample Datasets Included

You can immediately test the platform using sample files in the `data/` folder:
- **`glass.csv`**: Fast 10-feature numerical dataset ideal for instant validation.
- **`sample_data.csv`**: Real estate pricing dataset with mixed categorical and numeric attributes.
- **`Zomato Restaurant Dataset 2.csv`**: Multi-feature consumer dataset with ratings, locations, and costs.

---

## 📄 License
This project is licensed under the MIT License - feel free to use and adapt it.
