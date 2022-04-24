# stocktracker<br/>
This project uses python to analyze and co-relate the COVID-19 pandemic growth and its financial impact on the stock market in India and the U.S.A. 

**Description**:<br/>
In this project, I have used Yahoo finance APIs to get each month stock market data for specific stocks, covid19datahub to get COVID-19 cases data per country, stored both the datasets in CSV files. Then it reads the data from CSV files in Python Pandas data frame and performs cleaning of data. The cleaned data is then used toto plot the results to see the trend (e.g. spike in covid cases leading to a dip in stock prices) using Matplotlib (seaborn library). 

**Purpose**:<br/>
The main goal of this project was for me to learn python programming language on some real problem. Through this problem, I learned how to download data sets from Internet, save it in a file on local file system, perform data cleaning operations and then analyze it by plotting the same.  

**External modules used**: Please use "pip install" command to download the packages <br/>
  yfinance - to download stock ticker data of various stocks from internet in a given time range<br/>
  covid19dh - to download covid 19 cases of given country in a given timerange<br/>
  pandas - to save data in pandas dataframe<br/>
  matplotlib - to plot the results<br/>
  seaborn - for better plotting<br/>

**Important functions**:<br/>
main():  Called at the bottom - include the main function that goes through the above logic given in description by calling the various functions given below.<br/>
DownLoadTickerDataToCSV(): Downloads the data from startdate of ticker strings provided as input in tickerlist as dataframes and save them in a CSV file.<br/>
ReadTickerDataFromCSV(): Reads the ticker data from CSV file, cleans the data and return as data frame.<br/>
DownLoadCovidDataToCSV(): Downloads the data from startdate of covid 19 case from https://covid19datahub.io/ and save them in a CSV file.<br/>
ReadCovidDataFromCSV(): Read covid data from csv, cleans the data and returns as data frame.<br/>
TestYFinanceModule(): Sample function to test functionality of yfinance API - not used in real code!<br/>

**Sample output**:<br/>
The top graph shows changes in stock price of few tech firms on a monthly basis.<br/>
The bottom graph shows the increase in covid cases in USA and India.<br/>
Thing to co-relate: The sharper rise of covid cases (higher slope) as direct co-relation on market going down.<br/>
<img src="https://user-images.githubusercontent.com/99163025/164967291-31115671-b57d-4bcc-8a4e-278d9ca33940.jpeg">
