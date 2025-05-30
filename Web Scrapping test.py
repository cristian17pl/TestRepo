from re import findall
from unittest.mock import inplace

import yfinance as yf
import requests
import pandas as pd
from bs4 import BeautifulSoup

#Question 1
#Getting Tesla info from yfinance
tesla=yf.Ticker('TSLA')
#getting historic data
tesla_data=tesla.history(period='max')
#reseting the index
tesla_data.reset_index(inplace=True)
#printing with head function
#print(tesla_data.head())

#Question 2
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data=requests.get(url).text
#parse the response
soup=BeautifulSoup(html_data,'html.parser')
#create pd df
tesla_revenue=pd.DataFrame(columns=['Date','Revenue'])
#find quarterly table
table=soup.find_all('table')
quarterly_revenue_table = table[1]
#Assign values to the df
rows = quarterly_revenue_table.find_all("tr")
data = []
for row in rows[1:]:
    columns = row.find_all("td")
    Date = columns[0].text
    Revenue = columns[1].text
    data.append([Date, Revenue])
# Add to pd df
tesla_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])
#steps requested
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
# print tail
#print(tesla_revenue.tail())

#Question 3
Gamestop=yf.Ticker('GME')
#getting historic data
gme_data=Gamestop.history(period='max')
#reseting the index
gme_data.reset_index(inplace=True)
#printing with head function
#print(gme_data.head())

#Question 4
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data=requests.get(url).text
#parse the response
soup=BeautifulSoup(html_data,'html.parser')
#create pd df
gme_revenue=pd.DataFrame(columns=['Date','Revenue'])
#find quarterly table
table=soup.find_all('table')
quarterly_revenue_table = table[1]
#Assign values to the df
rows = quarterly_revenue_table.find_all("tr")
data = []
for row in rows[1:]:
    columns = row.find_all("td")
    Date = columns[0].text
    Revenue = columns[1].text
    data.append([Date, Revenue])
# Add to pd df
gme_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])
#steps requested
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
# print tail
#print(gme_revenue.tail())

#Question 5
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, title):
    # Convert 'Date' to datetime format in both df
    stock_data["Date"] = pd.to_datetime(stock_data["Date"])
    revenue_data["Date"] = pd.to_datetime(revenue_data["Date"])
    # Convert 'Revenue' to float for plotting
    revenue_data["Revenue"] = revenue_data["Revenue"].str.replace(r'[$,]', '', regex=True).astype(float)
    # Create plot
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data["Date"], stock_data["Close"], label="Stock Price", color="blue", linestyle="-")
    plt.plot(revenue_data["Date"], revenue_data["Revenue"], label="Quarterly Revenue", color="red", linestyle="--")
    # Formatting the graph
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

# Call the make_graph function
make_graph(tesla_data, tesla_revenue, "Tesla Revenue vs Stock")

#Question 5
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, title):
    # Convert 'Date' to datetime format in both df
    stock_data["Date"] = pd.to_datetime(stock_data["Date"])
    revenue_data["Date"] = pd.to_datetime(revenue_data["Date"])
    # Convert 'Revenue' to float for plotting
    revenue_data["Revenue"] = revenue_data["Revenue"].str.replace(r'[$,]', '', regex=True).astype(float)
    # Create plot
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data["Date"], stock_data["Close"], label="Stock Price", color="blue", linestyle="-")
    plt.plot(revenue_data["Date"], revenue_data["Revenue"], label="Quarterly Revenue", color="red", linestyle="--")
    # Formatting the graph
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

# Call the make_graph function
make_graph(gme_data, gme_revenue, "Gamestop Revenue vs Stock")