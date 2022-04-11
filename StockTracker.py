from pydoc_data.topics import topics
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
from covid19dh import covid19
import datetime
#import numpy as np
#import os
#from pathlib import Path

def TestYFinanceModule(): 
    '''Test function to test various methods of yfinance module'''
    # https://pypi.org/project/yfinance/
    msft = yf.Ticker("MSFT")

    # get stock info
    msft.info


    # get historical market data
    hist = msft.history(period="max")

    # show actions (dividends, splits)
    msft.actions

    # show dividends
    msft.dividends

    # show splits
    msft.splits

    # show financials
    msft.financials

    # show major holders
    msft.major_holders

    # show institutional holders
    msft.institutional_holders

    # show balance sheet
    msft.balance_sheet
    msft.quarterly_balance_sheet

    # show cashflow
    msft.cashflow
    msft.quarterly_cashflow

    # show earnings
    msft.earnings
    msft.quarterly_earnings

    # show sustainability
    msft.sustainability

    # show analysts recommendations
    msft.recommendations

    # show next event (earnings, etc)
    msft.calendar

    # show ISIN code - *experimental*
    # ISIN = International Securities Identification Number
    msft.isin

    # show options expirations
    msft.options

    # show news
    msft.news

    # get option chain for specific expiration
    opt = msft.option_chain('YYYY-MM-DD')
    # data available via: opt.calls, opt.puts

    return;
    #######

def DownLoadTickerDataToCSV(tickerlist, csvfilename, startdate):
    '''Downloads the data from startdate of ticker strings provided as input in tickerlist as dataframes and save them in a CSV file with filename as csvfilename'''
    tickerListOfDf = list()
    print("Downloading the ticker data from Internet to CSV file");
    for ticker in tickerlist: # for each ticker
        ticker_df = yf.download(ticker, group_by="Ticker", start=startdate, interval='1mo');
        ticker_df['Ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        tickerListOfDf.append(ticker_df) # append data frame for each ticker into a list
        #ticker_df.to_csv(f'ticker_{ticker}.csv')  # Write each ticker data to a separate file.  For example, ticker_MSFT.csv

    # combine all dataframes into a single dataframe
    tickersDf = pd.concat(tickerListOfDf)
    #print(tickersDf);

    # save the combined DF to CSV format file
    tickersDf.to_csv(csvfilename);

    return;
    ######

def ReadTickerDataFromCSV(tickerlist, csvfilename):
    '''Reads the ticker data from CSV file with filename as csvfilename. cleans the data and return as data frame'''
    print("Reading the ticker data from CSV file");
    # Read the CSV file into a DF
    tickerDf = pd.read_csv(csvfilename)
    #print(tickerDf);

    # Read from the set of ticker files and generate one Panda Dataframe
    # set the path to the files
    #p = Path("c:\users\samirj");
    # find the files; this is a generator, not a list
    #files = p.glob('ticker_*.csv')
    # read the files into a dataframe
    #tickerDf = pd.concat([pd.read_csv(file) for file in files])

    # Clean the data 
    print("Cleaning the ticker data");
    for x in tickerDf.index:
        ticker = str(tickerDf.loc[x, "Ticker"]);
        close_value = str(tickerDf.loc[x, "Close"]);
        datetimeobj=datetime.datetime.strptime(tickerDf.loc[x,"Date"], f"%Y-%m-%d"); # strip time and convert to datetime object
        if(close_value == "nan"  or datetimeobj.day != 1 or ticker not in tickerlist): #remove rows with empty value of Close OR day not equal to 1 as we want to take monthly data only OR ticker not in our inputlist
            tickerDf.drop(x, inplace = True); # delete the row from the data frame
    
    print("Cleaning done ...");
    #print(tickerDf);

    # Calculate the various percentages and add them as relevant column
    print("Computing more values on the ticker data");
    previous_ticker = "";
    previous_close = 0.0;
    for x in tickerDf.index:
        current_ticker = str(tickerDf.loc[x, "Ticker"])
        current_close = float(tickerDf.loc[x, "Close"]);
        if(current_ticker != previous_ticker): # Whenever new ticker is found
            previous_ticker = current_ticker;
            previous_close = current_close;
        percentage_change = (current_close - previous_close)*100/previous_close;
        #print(x, ticker, current_close, percentage_change);
        tickerDf.loc[x,"PercentageChange"] = percentage_change;
        previous_close = current_close;

    print("Computation done ...");
    print(tickerDf);        

    return tickerDf;
    ######

def DownLoadCovidDataToCSV(countrylist, csvfilename, startdate):
    countrycovidListOfDf = list();

    print("Downloading the covid data from Internet to CSV file"); # This API actually gets from https://covid19datahub.io/
    for country in countrylist: # for each country
        x, src = covid19(country, start=startdate);
        #print(x);
        countrycovidListOfDf.append(x);

    # combine all dataframes into a single dataframe
    coundtrycovidDf = pd.concat(countrycovidListOfDf)
    #print(coundtrycovidDf);

    # save the combined DF to CSV format file
    coundtrycovidDf.to_csv(csvfilename);
    return;
    ######

def ReadCovidDataFromCSV(csvfilename):
    '''Read covid data from csv (it was downloaded from https://covid19datahub.io/ in the above API'''
    
    #chdir is used to change the directory.
    #os.chdir('c:\\users\\samirj');
    
    print("Reading the covid data from CSV file");
    covidDf=pd.read_csv(csvfilename,usecols=['date','confirmed','iso_alpha_2', 'key_local']); # https://covid19datahub.io/,  https://github.com/covid19datahub/Python
    
    # Clean the data 
    print("Cleaning the covid data");
    for x in covidDf.index:
        key_local_value = str(covidDf.loc[x, "key_local"]);
        confirmed_value = str(covidDf.loc[x, "confirmed"]);
        datetimeobj=datetime.datetime.strptime(covidDf.loc[x,"date"], f"%Y-%m-%d"); # strip time and convert to datetime object
        if(key_local_value != "nan" or confirmed_value == 'nan' or datetimeobj.day != 1): #remove rows for state level data in key_local OR empty value of confirmed OR day not equal to 1 as we want to take monthly data only
            covidDf.drop(x, inplace = True); # delete the row from the data frame
    
    print("Cleaning done ...");
    #print(covidDf);
    
    # Calculate the various percentages and add them as relevant column
    print("Computing more values on the covid data");
    previous_key_local_value = "";
    previous_confirmed_value = 0.0;
    for x in covidDf.index:
        current_key_local_value = str(covidDf.loc[x, "key_local"])
        current_confirmed_value = float(covidDf.loc[x, "confirmed"]);
        if(current_key_local_value != previous_key_local_value): # Whenever new country is found
            previous_key_local_value = current_key_local_value;
            previous_confirmed_value = current_confirmed_value;
        percentage_change = (current_confirmed_value - previous_confirmed_value)*100/previous_confirmed_value;
        #print(x, ticker, current_close, percentage_change);
        covidDf.loc[x,"PercentageChange"] = percentage_change;
        previous_confirmed_value = current_confirmed_value;

    print("Computation done ...");
    print(covidDf);        

    return covidDf;
    ######

def main():
    '''Main function'''
    ######### Stock Market Related Code ################
    tickerList = ['AAPL', 'MSFT'];
    tickerFileName='tickerdata.csv';
    startdate = "2020-02-01";

    #Download from Internet to CSV File
    #DownLoadTickerDataToCSV(tickerList, tickerFileName, startdate);

    #Read the CSF file into Data frame
    tickerDf = ReadTickerDataFromCSV(tickerList, tickerFileName);
    #print(tickerDf);

    #Plot the data frame
    plt.subplot(2, 1, 1);
    sns.lineplot(x = 'Date', y = 'Close', data=tickerDf, hue='Ticker'); # https://seaborn.pydata.org/generated/seaborn.lineplot.html

    # Old way of plotting - not using
    #print(tickerDf.loc[tickerDf['Ticker'].isin(tickerList)]);
    #for ticker in tickerList:
        #print("Ticker Data");
        #print(tickerDf.loc[tickerDf['Ticker'] == ticker]);  # https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values#:~:text=To%20select%20rows%20whose%20column%20value%20equals%20a,value%20is%20in%20an%20iterable%2C%20some_values%2C%20use%20isin%3A
        #tickerDf.loc[tickerDf['Ticker'] == ticker].plot(kind = 'line', x = 'Date', y = 'Close', label = ticker); # makes separate plot for each iteration in the loop


    ######### Covid Related Code ################
    startdate = "2020-02-01";
    countryList = ['IN', 'USA']; # List of ISO code of country - https://github.com/covid19datahub/COVID19/blob/master/inst/extdata/db/ISO.csv
    covidFileName = "coviddata.csv";

    #Download from Internet to CSV File
    #DownLoadCovidDataToCSV(countryList, covidFileName, startdate);

    #Read the CSF file into Data frame (it was downloaded from https://covid19datahub.io/)
    covidDf = ReadCovidDataFromCSV(covidFileName);
    #print(covidDf);

    #Plot the data frame
    
    plt.subplot(2, 1, 2);
    sns.lineplot(x = 'date', y = 'confirmed', data=covidDf, hue='iso_alpha_2'); # https://seaborn.pydata.org/generated/seaborn.lineplot.html

    # Old way of plotting - not using
    #covidDf.plot(kind = 'line', x = 'date', y = 'confirmed', label = 'ConfirmedCases'); # Old way

    # Plot all the graphs/charts on the display
    plt.legend();
    plt.show();

    return;
    ######

# Call the main function
main();

