import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

# App initialization
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        'background': 'linear-gradient(to bottom, #333, #666)',
        'color': 'white',
        'padding': '20px',
        'textAlign': 'center',
    },
    children=[
        html.H1("Stock Price Prediction with GBM", style={'color': 'white'}),
        
        # Input components
        html.Div(
            style={'margin-bottom': '20px'},
            children=[
                html.Label("Enter Stock Ticker:"),
                dcc.Input(id="stock-input", type="text", value="AAPL", style={'color': 'black'}),
            ],
        ),
        
        html.Div(
            style={'margin-bottom': '20px'},
            children=[
                html.Label("Fetch Historical Data for:"),
                dcc.Dropdown(
                    id="time-input",
                    options=[
                        {'label': 'Last 1 Year', 'value': 252},
                        {'label': 'Last 6 Months', 'value': 126},
                        {'label': 'Last Quarter', 'value': 63},
                        {'label': 'Last 30 Days', 'value': 30},
                        {'label': 'Last Week', 'value': 5},
                    ],
                    value=252,
                    style={'backgroundColor': 'grey', 'color': 'black'},  # Set the text color to black
                ),
            ],
        ),
        
        html.Div(
            style={'margin-bottom': '20px'},
            children=[
                html.Label("Adjust Volatility:"),
                dcc.Slider(
                    id="volatility-slider",
                    min=0.01,
                    max=1.0,
                    step=0.01,
                    value=0.2,
                    marks={i: f"{i:.2f}" for i in np.arange(0.01, 1.01, 0.1)},
                ),
            ],
        ),
        
        # Output graph
        dcc.Graph(id="gbm-graph", style={'backgroundColor': 'lightgrey'}),
    ]
)

# Callback to update the graph
@app.callback(
    Output("gbm-graph", "figure"),
    [
        Input("stock-input", "value"),
        Input("time-input", "value"),
        Input("volatility-slider", "value"),
    ],
)
def update_graph(stock_ticker, time_frame, selected_volatility):
    # Calculate start date based on the current date minus the specified number of days
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=time_frame)).strftime('%Y-%m-%d')
    
    # Fetch historical stock data
    stock_data = yf.download(stock_ticker, start=start_date, end=end_date)
    
    # Calculate daily returns
    daily_returns = stock_data['Adj Close'].pct_change().dropna()
    
    # Calculate GBM parameters
    mu = daily_returns.mean() * 252
    sigma = daily_returns.std() * np.sqrt(252)
    
    # Generate GBM simulation
    t = np.arange(1, len(daily_returns) + 1)
    simulated_prices = [stock_data['Adj Close'].iloc[0]]
    
    for _ in range(1, len(t)):
        drift = mu * (1 / 252)
        diffusion = selected_volatility * np.sqrt(1 / 252) * np.random.normal(0, 1)
        price = simulated_prices[-1] * np.exp(drift + diffusion)
        simulated_prices.append(price)
    
    # Create figure
    figure = {
        'data': [
            {'x': stock_data.index, 'y': stock_data['Adj Close'], 'type': 'line', 'name': 'Actual Prices'},
            {'x': stock_data.index, 'y': simulated_prices, 'type': 'line', 'name': 'Simulated Prices'},
        ],
        'layout': {'title': f'GBM Simulation for {stock_ticker}', 'xaxis': {'title': 'Date'}, 'yaxis': {'title': 'Stock Price'}}
    }
    
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
