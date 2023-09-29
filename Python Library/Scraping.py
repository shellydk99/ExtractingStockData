#Downloading And Scraping The Contents of A Web Page
url = "http://www.ibm.com"

data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
  for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
      print(link.get('href'))
    
#Scrape all images tags
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))

#Scrape data from HTML tables
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
import pandas as pd
url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')
len(tables)
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
print(tables[table_index].prettify())
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

#Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
pd.read_html(str(tables[5]), flavor='bs4')
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
population_data_read_html

#Scrape data from HTML tables into a DataFrame using read_html
dataframe_list = pd.read_html(url, flavor='bs4')
len(dataframe_list)
dataframe_list[5]
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
