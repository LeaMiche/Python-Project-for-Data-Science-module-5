# Question 1
#yfinance and tesla

import yfinance as yf # Download historical data for a stock

tesla = yf.Ticker("MSFT")
tesla_data = tesla.history(period="max")

#print(tesla_data.head()) # Display the downloaded data

tesla_data.reset_index(inplace = True)
#print(tesla_data.head())

#==============================================================================

# Question 2
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data=requests.get(url).text
soup = BeautifulSoup(html_data , "html.parser")

read_html_pandas_data = pd.read_html(url)

tesla_revenue = read_html_pandas_data[1] #take the Date and Revenue

tesla_revenue["Tesla Quarterly Revenue (Millions of US $).1"] = tesla_revenue["Tesla Quarterly Revenue (Millions of US $).1"].str.replace(',|\$',"")
tesla_revenue = tesla_revenue[tesla_revenue["Tesla Quarterly Revenue (Millions of US $).1"] != ""]
tesla_revenue.dropna(inplace=True)

#print(tesla_revenue.tail())

#=============================================================================
#Question 3 GameStop

GameShop = yf.Ticker("GME")
gme_data = GameShop.history(period="max")
gme_data.reset_index(inplace=True)
#print(gme_data.head())

#=============================================================================
#Question 4 

url1 =" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data2 = requests.get(url1).text
soup1 = BeautifulSoup(html_data2 , "html.parser")

read_html_pandas_data1 = pd.read_html(url1)

gme_revenue= read_html_pandas_data1[1] #take the Date and Revenue

gme_revenue["GameStop Quarterly Revenue (Millions of US $).1"] = gme_revenue["GameStop Quarterly Revenue (Millions of US $).1"].str.replace(',|\$',"")
gme_revenue = gme_revenue[gme_revenue["GameStop Quarterly Revenue (Millions of US $).1"] != ""]
gme_revenue.dropna(inplace=True)

#print(gme_revenue.tail())

#=============================================================================
#Question 5
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

make_graph(tesla_data, tesla_revenue, 'Tesla')










