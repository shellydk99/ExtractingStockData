Analyzing Historical Stock/Revenue Data and Building a Dashboard
Extracting and Visualizing Stock Data

!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y
!pip install nbformat==4.2.0

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Define Graphing Function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
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

#Use yfinance to Extract Stock Data
        tesla = yf.Ticker("TSLA")
        tesla_data = tesla.history(period="max") #extract stock information and save it in a dataframe
        tesla_data.reset_index(inplace=True)
        tesla_data.head()

#Use Webscraping to Extract Tesla Revenue Data
        url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
        html_data  = requests.get(url).text
        soup = BeautifulSoup(html_data, "html.parser") #Parse the html data using beautiful_soup
        soup.find_all('title')

        beautiful_soup.find_all("tbody")[1]
        tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"]) #extract table into a dataframe
        for row in soup.find_all("tbody")[1].find_all("tr"):
            col = row.find_all("td")
            date = col[0].text
            revenue = col[1].text
            tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
        
        tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"") #delete dollars and coma
        tesla_revenue.dropna(inplace=True)
        tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
        
        last_5_rows = tesla_revenue.tail(5) #print last 5 rows
        print(last_5_rows)

#use yfinance to Extract Stock Data
        GameStop = yf.Ticker("GME")
        gme_data = GameStop.history(period="max")
        gme_data.reset_index(inplace=True)
        gme_data.head()

#Use Websraping to Extract  GME revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('tittle')

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"]) #extract table into a dataframe
for row in soup.find("tbody")[1].find_all("tr"):
            col = row.find_all("td")
            date = col[0].text
            revenue = col[1].text.replace("$", "").replace(",", "")
            gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
    
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
last_5_rows = gme_revenue.tail(5)
print(last_5_rows)

#Plot Tesla Stock Graph
make_grapgh(tesla_data, tesla revenue, 'tesla')

#Plot GameStop Stock Graph
make_graph(gme_data, gme_revenue, 'GameStop')
