# Extracting Data using a Web Scraping
```r{}
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y 
!pip install lxml==4.6.4

import pandas as pd
import requests
from bs4 import BeautifulSoup
```
## Using Webscraping to Extract Stock Data
***Step-1 Send an HTTP Request to the webpage***
```r{}
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
```
The requests.get() method takes a URL as its first argument, which specifies the location of the resource to be retrieved. In this case, the value of the url variable is passed as the argument to the requests.get() method, as we've stored a webpage URL in a url variable.

we have used .text method for extracting the HTML content as a string in order to make it readable.
```r{}
data  = requests.get(url).text
print(data)
```
***Step-2 Parse the HTML content***
## What is parsing?
In simple words, parsing refers to the process of analyzing a string of text or a data structure, usually following a set of rules or grammar, to understand its structure and meaning. Parsing involves breaking down a piece of text or data into its individual components or elements, and then analyzing those components to extract the desired information or to understand their relationships and meanings
## Parse the data using BeautifulSoup library
Create a new Beautiful soup object.
Note:- To create a Beautiful Soup object in Python, you need to pass two arguments to its constructor:
The HTML or XML content that you want to parse as a string.
The name of the parser that you want to use to parse the HTML or XML content. This argument is optional, and if you don't specify a parser, Beautiful Soup will use the default HTML parser included with the library. here in this lab we are using "html5lib" parser.
```r{}
soup = BeautifulSoup(data, 'html5lib')
```
***Step-3 Identify the HTML tags***
```r{}
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
```
## Working on HTML Table
These are the following tags which are used while creating HTML tables.
```r{}
<table> tag: This tag is root tag used to define the start and end of the table. All the content of the table is enclosed within these tags.
<tr> tag: This tag is used to define a table row. Each row of the table is defined within this tag.
<td> tag: This tag is used to define a table cell. Each cell of the table is defined within this tag. You can specify the content of the cell between the opening and closing tags.
<th> tag: This tag is used to define a header cell in the table. The header cell is used to describe the contents of a column or row. By default, the text inside a tag is bold and centered.
<tbody> tag: This is the main content of the table, which is defined using the tag. It contains one or more rows of elements.
```

***Step-4 Use BaautifulSoup method for extracting data***

We will use find() and find_all() methods of the BeautifulSoup object to locate the table body and table row respectively in the HTML.
The find() method will return particular tag content.
The find_all() method returns a list of all matching tags in the HTML
```r{}
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
```
***Step-5 Print the Extracted Data***
```r{}
netflix_data.head()
```
![Screenshot (1344)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/0afb469f-8392-4ed0-b811-181f989acf16)

# Extracting data using pandas library
## read_html pandas library
pd.read_html(url) is a function provided by the pandas library in Python that is used to extract tables from HTML web pages. It takes in a URL as input and returns a list of all the tables found on the webpage
```r{}
read_html_pandas_data = pd.read_html(url)
```
Or we can convert the BeautifulSoup object to a string
```r{}
read_html_pandas_data = pd.read_html(str(soup))
```
Because there is only one table on the page, we just take the first table in the list returned
```r{}
netflix_dataframe = read_html_pandas_data[0]
netflix_dataframe.head()
```
![Screenshot (1345)](https://github.com/shellydk99/ExtractingStockData/assets/126668898/b69a325a-aca7-49cb-9260-acfedb7b2689)
