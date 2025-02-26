# Stock Price Prediction with Geometric Brownian Motion (GBM)  

## About This Project  

This is a **Dash-powered web application** that simulates **stock price movements** using the **Geometric Brownian Motion (GBM) model**. The app allows users to fetch historical stock price data, adjust volatility parameters, and visualize simulated future price trends alongside actual stock prices.  

## Features  
- 📈 **Fetch real-time stock data** from Yahoo Finance (`yfinance`).  
- 🔍 **User input for stock ticker** to analyze different stocks.  
- 📅 **Customizable historical time frame** (Last 1 year, 6 months, quarter, etc.).  
- 🎛 **Adjustable volatility slider** to modify price movement intensity.  
- 🔄 **GBM-based simulation** of stock prices using historical returns.  
- 📊 **Interactive graph** displaying actual vs. simulated prices.  

## Technologies Used  
- 🐍 **Python**  
- 📦 **Dash (Plotly)** for interactive UI  
- 🔗 **Yahoo Finance API (`yfinance`)** for real-time stock data  
- 📊 **NumPy** for stochastic modeling  
- 📝 **Pandas** for data handling  

## How It Works  
1. **Enter a stock ticker** (e.g., AAPL, TSLA, GOOG).  
2. **Select a historical time frame** for fetching stock data.  
3. **Adjust volatility** using the slider.  
4. **The app fetches real stock prices** and simulates future movements using the **GBM model**.  
5. **The interactive graph** displays both actual and simulated stock prices.  

## Run the Project Locally  
1. **Clone this repository:**  
   ```bash
   git clone https://github.com/your-username/stock-gbm-simulation.git
   cd stock-gbm-simulation
