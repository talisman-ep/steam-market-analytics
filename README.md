# 🔫 Steam Market Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

An interactive analytics dashboard designed to monitor and analyze CS2 skin prices in real-time. This tool serves as the frontend interface for a high-load scraping system, visualizing market trends and helping traders identify profitable opportunities.

🔗 **[Live Demo](https://share.streamlit.io/)** *(Insert your link here after deployment)*

---

## ⚡ Key Features

* **📈 Market Overview:** Real-time visualization of price trends using interactive charts.
* **🔍 Smart Filtering:** Advanced search functionality to filter items by name, price range, and risk level.
* **📊 KPI Metrics:** Instant calculation of average market price, highest value items, and volume stats.
* **📱 Responsive Design:** Fully optimized for both desktop and mobile devices via Streamlit.

## 🛠 Tech Stack

* **Backend Logic:** Python 3.10
* **Frontend/UI:** Streamlit
* **Data Processing:** Pandas
* **Visualization:** Plotly Express
* **Data Source:** PostgreSQL (Live) / CSV Snapshot (Demo)

## 🚀 Installation & Setup

To run this dashboard locally on your machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/steam-dashboard.git](https://github.com/YOUR_USERNAME/steam-dashboard.git)
    cd steam-dashboard
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**
    ```bash
    streamlit run dashboard.py
    ```

## 📂 Project Architecture

This dashboard is part of a larger ecosystem:
1.  **Scraper Service (Backend):** Asynchronously collects data from Steam Community Market.
2.  **PostgreSQL Database:** Stores historical price data and item metadata.
3.  **Streamlit Dashboard (Frontend):** Connects to the database to render insights for the end-user.

Star ⭐ this repo if you find it useful!
