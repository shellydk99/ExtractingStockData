## Web Scraping Lab
```{r Web Scraping Lab}
#Install Library
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y

from bs4 import BeautifulSoup                  #this module helps in web scrapping.
import requests                                #this module helps us to download a web page
```
## BeautifulSoup object
 ### String in The Variable HTML 
```{r String in the variable HTML}
  html ="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
  soup = BeautifulSoup(html, "html.parser")    #parse a document
  print(soup.prettify())                       #display the HTML in the nested structure
```

### Tags
```{r Tags}
  tag_object=soup.title        
  print("tag object:",tag_object)              #show the title  of the page
  print("tag object type:",type(tag_object))   #see the tag type
  tag_object=soup.h3                           #the tag more than one
  tag_object
```

***Children, parents, and siblings***
```{r}
  tag_child =tag_object.b                      #tag object is a tree of objects
  tag_child
  parent_tag=tag_child.parent
  parent_tag                                   #this identical to tag_object

  tag_object.parent                            #tag_object parent is the body element
  sibling_1=tag_object.next_sibling            #tag_object sibling is the paragraph element
  sibling_1
  sibling_2=sibling_1.next_sibling             #sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object
  sibling_2
```

***HTML Attributes***
```{r}
  tag_child['id']                              #tag's attributes
  tag_child.attrs                              #access dictionary
  tag_child.get('id')                          #obtain the content if the attribute of the tag using the Python get() method.
```

***Navigable String***
```{r}
  tag_string=tag_child.string
  tag_string                                  
  type(tag_string)                             #verify the type is Navigable String

  unicode_string = str(tag_string)
  unicode_string
```

## Filter
Filters allow to find complex patterns, the simplest filter is a string. In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string

```{r}
  table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
  table_bs = BeautifulSoup(table, "html.parser")
```
### Find All
The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

***Name***
When we set the name parameter to a tag name, the method will extract all the tags with that name and its children
```{r}
  table_rows=table_bs.find_all('tr')
  table_rows
  first_row =table_rows[0]                  #The result is a Python Iterable just like a list, each element is a tag object:
  first_row
  print(type(first_row))                    #The type is tag
  first_row.td
  for i,row in enumerate(table_rows):       #If we iterate through the list, each element corresponds to a row in the table:
    print("row",i,"is",row)
```
As row is a cell object, we can apply the method find_all to it and extract table cells in the object cells using the tag td, this is all the children with the name td. The result is a list, each element corresponds to a cell and is a Tag object, we can iterate through this list as well. We can extract the content using the string attribute.
```{r}
  for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

    list_input=table_bs .find_all(name=["tr", "td"])    #list to match against any item
      list_input
```

### Attribute
If the argument is not recognized it will be turned into a filter on the tag’s attributes. For example the id argument, Beautiful Soup will filter against each tag’s id attribute. For example, the first td elements have a value of id of flight, therefore we can filter based on that id value.
```{r}
  table_bs.find_all(id="flight")
  list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")      #find all the elements that have links
  list_input
  table_bs.find_all(href=True)                                                    #If we set the href attribute to True, regardless of what the value is
```

***String***
```{r}
table_bs.find_all(string="Florida")                                        #With string we can search for strings instead of tags
```
***Find***
The find_all() method scans the entire document looking for results, it’s if you are looking for one element you can use the find() method to find the first element in the document.
```{r}
  two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
  two_tables_bs= BeautifulSoup(two_tables, 'html.parser')                 #We create a BeautifulSoup object two_tables_bs
  two_tables_bs.find("table")                                             #We can find the first table using the tag name table
  two_tables_bs.find("table",class_='pizza')                              #We can filter on the class attribute to find the second table, but because class is a keyword in Python, we add an underscore.
```
### Downloading and Scraping The Contents of A Web Page
```{r}
  url = "http://www.ibm.com"                                              #We Download the contents of the web page
  data  = requests.get(url).text
  soup = BeautifulSoup(data,"html.parser")                                #create a soup object using the variable 'data'

  for link in soup.find_all('a',href=True):                               #in html anchor/link is represented by the tag <a>
    print(link.get('href'))
```
***Scrape all images Tags***
```{r}
  for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
```
***Scrape data from HTML tables***
```{r}
  url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"     #The below url contains an html table with data about colors and color codes.
  data  = requests.get(url).text                                      #get the contents of the webpage in text format and store in a variable called data
  soup = BeautifulSoup(data,"html.parser")
  table = soup.find('table')                                          #find a html table in the web page, in html table is represented by the tag <table>

  #Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
```
***Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas***
```{r}
  import pandas as pd
  url = "https://en.wikipedia.org/wiki/World_population"
  data  = requests.get(url).text          #get the contents of the webpage in text format and store in a variable called data
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
```

***Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html***
```{r}
  pd.read_html(str(tables[5]), flavor='bs4')                                #We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4
  pd.read_html(str(tables[5]), flavor='bs4')
  population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0] #The function read_html always returns a list of DataFrames so we must pick the one we want out of the list
  population_data_read_html
```

***Scrape data from HTML tables into a DataFrame using read_html***
```{r}
  dataframe_list = pd.read_html(url, flavor='bs4')
  len(dataframe_list)
  dataframe_list[5]
  pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]    #We can also use the match parameter to select the specific table we want. If the table contains a string matching the text it will be read.
```
