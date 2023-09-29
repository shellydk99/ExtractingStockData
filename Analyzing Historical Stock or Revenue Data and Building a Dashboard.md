# Analyzing Historical Stock/Revenue
```r{}
!pip install yfinance==0.1.67
!mamba install bs4==4.10.0 -y
!pip install nbformat==4.2.0

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```
## Define Graphing Function
In this section, we define the function make_graph
```r{}
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
```
## Use yfinance to Extract Stock Data
Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA
```r{}
tesla = yf.Ticker("TSLA")  
```
Using the ticker object and the function history extract stock information and save it in a dataframe named tesla_data. Set the period parameter to max so we get information for the maximum amount of time.
```r{}
tesla_data = tesla.history(period="max")           #extract stock information and save it in a dataframe
```
Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and display the first five rows of the tesla_data dataframe using the head function.
```r{}
  tesla_data.reset_index(inplace=True)
  tesla_data.head()
```
![Screenshot (1338)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/f681547f-a930-4224-867b-f61922e86899)

## Use Webscraping to Extract Tesla Revenue Data
Use the requests library to download the webpage
```r{}
 url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
```
Parse the html data using beautiful_soup.
```r{}
soup = BeautifulSoup(html_data, "html.parser")
```
Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue
```r{}
tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)
```
Remove an null or empty strings in the Revenue column
```r{}
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
```
Display the last 5 row of the tesla_revenue dataframe using the tail function
```r{}
tesla_revenue.tail()
```
![Screenshot (1339)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/60484b97-60b5-497b-935c-b1b4c0cb6239)

## Use yfinance to Extract Stock Data
Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is GME.
```r{}
GameStop = yf.Ticker("GME")
```
Using the ticker object and the function history extract stock information and save it in a dataframe named gme_data. Set the period parameter to max so we get information for the maximum amount of time.
```r{}
gme_data = GameStop.history(period = 'max')
```
Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the first five rows of the gme_data dataframe using the head function
```r{}
![Screenshot (1340)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/91eda9fb-9c82-4215-b81c-4ba7fa715a4f)

## Use Webscraping to Extract GME Revenue Data
Use the requests library to download the webpage
```r{}
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
```
Parse the html data using beautiful_soup
```r{}
soup = BeautifulSoup(html_data, "html.parser")
```
Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`.
```r{}
gme_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)
```
Display the last five rows of the gme_revenue dataframe using the tail function
```r{}
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue.tail()
```
![Screenshot (1341)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/2536a306-7f87-474e-afc1-45cd03705514)

## Plot Tesla Stock Grapgh
```r{}
make_graph(tesla_data, tesla_revenue, 'Tesla')
```
![Screenshot (1342)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/5056c3c4-d26d-4b8e-8b69-0ece314eb32b)

## Plot GameStop Stock Graph
```r{}
make_graph(gme_data, gme_revenue, 'GameStop')
````
![Screenshot (1343)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/2b355e32-e8b9-44ce-bf28-0743b2743c35)
