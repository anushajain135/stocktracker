# stocktracker
This project uses python to analyze and co-relate the COVID-19 pandemic growth and its financial impact on the stock market in India and the U.S.A. 

Description:
In this project, I have used Yahoo finance APIs to get each month stock market data for specific stocks, covid19datahub to get COVID-19 cases data per country, stored both the datasets in CSV files. Then it reads the data from CSV files in Python Pandas data frame and performs cleaning of data. The cleaned data is then used toto plot the results to see the trend (e.g. spike in covid cases leading to a dip in stock prices) using Matplotlib (seaborn library). 

Purpose:
The main goal of this project was for me to learn python programming language on some real problem. Through this problem, I learned how to download data sets from Internet, save it in a file on local file system, perform data cleaning operations and then analyze it by plotting the same.  

External modules used: Please use "pip install" command to download the packages
yfinance - to download stock ticker data of various stocks from internet in a given time range
covid19dh - to download covid 19 cases of given country in a given timerange
pandas - to save data in pandas dataframe
matplotlib - to plot the results
seaborn - for better plotting

Important functions:
main():  Called at the bottom - include the main function that goes through the above logic given in description by calling the various functions given below.
DownLoadTickerDataToCSV(): Downloads the data from startdate of ticker strings provided as input in tickerlist as dataframes and save them in a CSV file.
ReadTickerDataFromCSV(): Reads the ticker data from CSV file, cleans the data and return as data frame.
DownLoadCovidDataToCSV(): Downloads the data from startdate of covid 19 case from https://covid19datahub.io/ and save them in a CSV file.
ReadCovidDataFromCSV(): Read covid data from csv, cleans the data and returns as data frame.
TestYFinanceModule(): Sample function to test functionality of yfinance API - not used in real code!

Sample output:
[Sample-Results](https://user-images.githubusercontent.com/99163025/164967291-31115671-b57d-4bcc-8a4e-278d9ca33940.jpeg)
