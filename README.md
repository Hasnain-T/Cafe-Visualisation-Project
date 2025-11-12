# ☕ Cafe Sales ETL & Dashboard

A data engineering mini-project that performs **ETL (Extract, Transform, Load)** on café sales data and automatically launches an interactive **Streamlit dashboard** for visual analysis.

---

## 📁 Project Structure

- project_root/
    - │
    - ├── data/
    - │ ├── raw_data.csv # Input dataset (raw sales data)
    - │ └── cleaned_data.csv # Output dataset after ETL
    - │
    - └── src/
    - ├── main.py # Main ETL pipeline + dashboard launcher
    - ├── cafe_dashboard.py # Streamlit dashboard app
    - ├── extract.py # Extract data from CSV
    - ├── transform.py # Clean and transform data
    - ├── load.py # Save cleaned data to CSV
    - ├── load_to_db.py # Load data into PostgreSQL
    - ├── style.py # Custom terminal output styling

---

## 🚀 Features

- **Extract:** Reads raw café sales data from a CSV file  
- **Transform:** Cleans and standardises the dataset  
- **Load:** Saves the cleaned data into a new CSV and PostgreSQL database  
- **Visualise:** Automatically launches a Streamlit dashboard with KPIs and interactive charts  

---

## 🧠 ETL Flow

1. **Extract** → Reads `raw_data.csv`
2. **Transform** → Cleans columns, formats prices, handles nulls, etc.
3. **Load** → Saves cleaned data to:
   - `cleaned_data.csv`
   - PostgreSQL database (via `load_to_db.py`)
4. **Dashboard Launch** → Opens `cafe_dashboard.py` in your browser

---

## 📊 Dashboard Overview

The Streamlit dashboard provides:

- 💰 **Total Revenue per Drink**
- 🛒 **Total Sales per Branch**
- ☕ **Average Drink Price Across Branches**
- 🏬 **Branch Count**
- 📈 Sales Over Time
- 🥤 Drink Popularity by Branch
- 💳 Branch vs Payment Type (Total Sales)
- 💳 Payment Type Distribution
- 💳 Payment Method Share
- 🌡️ Heatmap: Average Prices per Branch

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
- git clone https://github.com/Hasnain-T/Cafe-Visualisation-Project
- cd Cafe-Visualisation-Project


### 2️⃣ Create and Activate a Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Verify Folder Structure

Ensure src/main.py and src/cafe_dashboard.py exist, and data/raw_data.csv is available.

## 🐳 Docker Setup (Optional but Recommended)

You can containerize the entire ETL and database setup for consistent development.

### 1️⃣ Install Docker & Docker Compose

- Download Docker Desktop

- Ensure Docker Engine and Compose are running.

### 2️⃣ Example docker-compose.yml

- Check this file in your project root:
    - docker-compose.yml

### 3️⃣ Run the containers
- docker-compose up -d

### 4️⃣ Access Adminer

- Once running, open your browser and visit:
    - http://localhost:8080

 - Adminer login:
    - Field:	Value
    - System:	PostgreSQL
    - Server:	postgres
    - Username:	cafe_user
    - Password:	cafe_pass
    - Database:	cafe_db

## ▶️ Run the ETL Pipeline + Dashboard

- From the src directory:
    - python main.py OR py main.py OR python3 main.py


- The ETL process will extract, transform, and load your data.

- Once complete, the Streamlit dashboard will automatically launch in your browser at:
    - http://localhost:8501

### ⚙️ Configuration

- Update these paths in main.py if needed:
    - file_path = "../data/raw_data.csv"
    - cleaned_file_path = "../data/cleaned_data.csv"


### Database connection settings can be adjusted inside load_to_db.py.

### 🧩 Dependencies

- Key Python packages used:

    - pandas

    - streamlit

    - plotly

    - psycopg2

    - os, sys, subprocess

### 🧾 Example Output (Terminal)
    - [INFO] Extraction Complete.
    - [INFO] Transformation Complete.
    - [INFO] Data successfully saved to cleaned_data.csv
    - [INFO] Data successfully loaded into PostgreSQL.
    - [INFO] Launching Streamlit Dashboard...