
#Importing all the libraries
from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt


def calculate_protfolio(list_of_ticks, img_name):
    #Select stocks, start year and end year, stock number has no known limit
    ## Insert Parmater
    start_year = '2009-1-1'
    end_year = '2021-04-01'
    Num_porSimulation = 100000  # Number of Portfolio that will build for simulator

    ## End Insert Parameter
    #Select stocks, start year and end year, stock number has no known limit


    #Building the DataBase
    yf.pdr_override()
    frame = {}
    for stock in list_of_ticks:
        data_var = pdr.get_data_yahoo(stock, start_year,end_year)['Adj Close']
        data_var.to_frame()
        frame.update({stock: data_var})
    # End Insert Adj Close To DataBase

    import pandas as pd
    #Mathematical calculations Return Daily And annualy, creation of Number portfolios,
    table = pd.DataFrame(frame)
    returns_daily = table.pct_change()
    returns_annual = ((1+ returns_daily.mean())**250) - 1


    # get daily and covariance of returns of the stock
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250

    # empty lists to store returns, volatility and weights of imiginary portfolios
    port_returns = []
    port_volatility = []
    sharpe_ratio = []
    stock_weights = []

    # set the number of combinations for imaginary portfolios
    num_assets = len(list_of_ticks)
    num_portfolios = Num_porSimulation                                    # Change porfolio numbers here

    #set random seed for reproduction's sake
    np.random.seed(101)

    # populate the empty lists with each portfolios returns,risk and weights
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, returns_annual)
        returns = np.dot(weights, returns_annual)
        # calculation the Standard Deviation of portfolio.
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
         # calculation the sharpe of portfolio.
        sharpe = returns / volatility
        sharpe_ratio.append(sharpe)
        # Percent Conversion
        port_returns.append(returns*100)
        port_volatility.append(volatility*100)
        stock_weights.append(weights)

    # a dictionary for Returns and Risk values of each portfolio
    portfolio = {'Returns': port_returns,
                 'Volatility': port_volatility,
                 'Sharpe Ratio': sharpe_ratio}

    # extend original dictionary to accomodate each ticker and weight in the portfolio
    for counter,symbol in enumerate(list_of_ticks):
        portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

    # make a nice dataframe of the extended dictionary
    df = pd.DataFrame(portfolio)

    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in list_of_ticks]

    # reorder dataframe columns
    df = df[column_order]

    # plot frontier, max sharpe & min Volatility values with a scatterplot
    # find min Volatility & max sharpe values in the dataframe (df)
    min_volatility =df['Volatility'].min()
    #min_volatility1 = df['Volatility'].min()+1
    max_sharpe = df['Sharpe Ratio'].max()
    max_return = df['Returns'].max()
    max_vol = df['Volatility'].max()
    # use the min, max values to locate and create the two special portfolios
    sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
    min_variance_port = df.loc[df['Volatility'] == min_volatility]
    max_returns = df.loc[df['Returns'] == max_return]
    max_vols = df.loc[df['Volatility'] == max_vol]


    # plot frontier, max sharpe & min Volatility values with a scatterplot
    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='green', marker='D', s=200)
    plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='orange', marker='D', s=200 )
    plt.scatter(x=max_vols['Volatility'], y=max_returns['Returns'], c='red', marker='D', s=200 )
    plt.style.use('seaborn-dark')

    plt.xlabel('Volatility (Std. Deviation) Percentage %')
    plt.ylabel('Expected Returns Percentage %')
    plt.title('Efficient Frontier')
    plt.subplots_adjust(bottom=0.4)
    # ------------------ Pritning 3 optimal Protfolios -----------------------
    #Setting max_X, max_Y to act as relative border for window size

    red_num = df.index[df["Returns"] == max_return]
    yellow_num = df.index[df['Volatility'] == min_volatility]
    green_num = df.index[df['Sharpe Ratio'] == max_sharpe]
    multseries = pd.Series([1,1,1]+[100 for stock in list_of_ticks], index=['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in list_of_ticks])
    with pd.option_context('display.float_format', '%{:,.2f}'.format):
        plt.figtext(0.2, 0.15, "Max returns Porfolio: \n" + df.loc[red_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='red', alpha=0.5), fontsize=11, style='oblique',ha='center', va='center', wrap=True)
        plt.figtext(0.45, 0.15, "Safest Portfolio: \n" + df.loc[yellow_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='yellow', alpha=0.5), fontsize=11, style='oblique', ha='center', va='center', wrap=True)
        plt.figtext(0.7, 0.15, "Sharpe  Portfolio: \n" + df.loc[green_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='green', alpha=0.5), fontsize=11, style='oblique', ha='center', va='center', wrap=True)
    plt.savefig(str(img_name) + '.png')


# calculate_protfolio(selected)

#
# import pandas as pd
# #Mathematical calculations, creation of 5000 portfolios,
# table = pd.DataFrame(frame)
# returns_daily = table.pct_change()
# returns_annual = ((1+ returns_daily.mean())**250) - 1
#
# # get daily and covariance of returns of the stock
# cov_daily = returns_daily.cov()
# cov_annual = cov_daily * 250
#
# # empty lists to store returns, volatility and weights of imiginary portfolios
# port_returns = []
# port_volatility = []
# sharpe_ratio = []
# stock_weights = []
#
# # set the number of combinations for imaginary portfolios
# num_assets = len(selected)
# num_portfolios = Num_porSimulation                                    # Change porfolio numbers here
#
# #set random seed for reproduction's sake
# np.random.seed(101)
#
# # populate the empty lists with each portfolios returns,risk and weights
# for single_portfolio in range(num_portfolios):
#     weights = np.random.random(num_assets)
#     weights /= np.sum(weights)
#     returns = np.dot(weights, returns_annual)
#     returns = np.dot(weights, returns_annual)
#     volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
#     sharpe = returns / volatility
#     sharpe_ratio.append(sharpe)
#     port_returns.append(returns*100)
#     port_volatility.append(volatility*100)
#     stock_weights.append(weights)
#
# # a dictionary for Returns and Risk values of each portfolio
# portfolio = {'Returns': port_returns,
#              'Volatility': port_volatility,
#              'Sharpe Ratio': sharpe_ratio}
#
# # extend original dictionary to accomodate each ticker and weight in the portfolio
# for counter,symbol in enumerate(selected):
#     portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]
#
# # make a nice dataframe of the extended dictionary
# df = pd.DataFrame(portfolio)
#
# # get better labels for desired arrangement of columns
# column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in selected]
#
# # reorder dataframe columns
# df = df[column_order]
#
# # plot frontier, max sharpe & min Volatility values with a scatterplot
# # find min Volatility & max sharpe values in the dataframe (df)
# min_volatility =df['Volatility'].min()
# #min_volatility1 = df['Volatility'].min()+1
# max_sharpe = df['Sharpe Ratio'].max()
# max_return = df['Returns'].max()
# max_vol = df['Volatility'].max()
# # use the min, max values to locate and create the two special portfolios
# sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
# min_variance_port = df.loc[df['Volatility'] == min_volatility]
# max_returns = df.loc[df['Returns'] == max_return]
# max_vols = df.loc[df['Volatility'] == max_vol]
#
#
# # plot frontier, max sharpe & min Volatility values with a scatterplot
# plt.style.use('seaborn-dark')
# df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
#                 cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
# plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='green', marker='D', s=200)
# plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='orange', marker='D', s=200 )
# plt.scatter(x=max_vols['Volatility'], y=max_returns['Returns'], c='red', marker='D', s=200 )
# plt.style.use('seaborn-dark')
#
# plt.xlabel('Volatility (Std. Deviation) Percentage %')
# plt.ylabel('Expected Returns Percentage %')
# plt.title('Efficient Frontier')
# plt.subplots_adjust(bottom=0.4)
# # ------------------ Pritning 3 optimal Protfolios -----------------------
# #Setting max_X, max_Y to act as relative border for window size
#
# red_num = df.index[df["Returns"] == max_return]
# yellow_num = df.index[df['Volatility'] == min_volatility]
# green_num = df.index[df['Sharpe Ratio'] == max_sharpe]
# multseries = pd.Series([1,1,1]+[100 for stock in selected], index=['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in selected])
# with pd.option_context('display.float_format', '%{:,.2f}'.format):
#     plt.figtext(0.2, 0.15, "Max returns Porfolio: \n" + df.loc[red_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='red', alpha=0.5), fontsize=11, style='oblique',ha='center', va='center', wrap=True)
#     plt.figtext(0.45, 0.15, "Safest Portfolio: \n" + df.loc[yellow_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='yellow', alpha=0.5), fontsize=11, style='oblique', ha='center', va='center', wrap=True)
#     plt.figtext(0.7, 0.15, "Sharpe  Portfolio: \n" + df.loc[green_num[0]].multiply(multseries).to_string(),bbox=dict(facecolor='green', alpha=0.5), fontsize=11, style='oblique', ha='center', va='center', wrap=True)
# plt.show()
#
# a= "Got Night"
# print(a)