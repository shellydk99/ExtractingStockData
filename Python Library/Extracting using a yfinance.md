# Extracting Stock Data Using a Python Library
```r{}
!pip install yfinance==0.2.4

import yfinance as yf
import pandas as pd
````
## Using the yfinance Library to Extract Stock Data
Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.
```r{}
  apple = yf.Ticker("AAPL")
  !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json
```
### Stock Info
Using the attribute info we can extract information about the stock as a Python dictionary
```r{}
 import json
    with open('apple.json') as json_file:
        apple_info = json.load(json_file)
        # Print the type of data variable    
        #print("Type:", type(apple_info))
    apple_info
  apple_info['country']                         #We can get the 'country' using the key country
```
### Extracting Share Price
A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time. Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
```r{}
  apple_share_price_data = apple.history(period="max")
```
The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
```r{}
  apple_share_price_data.head()
```
We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
```r{}
  apple_share_price_data.reset_index(inplace=True)
```
We can plot the Open price against the Date:
```r{}
  apple_share_price_data.plot(x="Date", y="Open")
```
