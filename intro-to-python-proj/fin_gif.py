import os
import datetime
import argparse

import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import MinMaxScaler
import yfinance as yf
import imageio

# Step 3
def download_data(ticker):
    """
    Function that downloads 1 month of ticker data
    input:
        ticker {str} --- 3-4 character ticker code

    returns:
        data {ndarray - float64} --- 1d numpy array of adjusted close prices
    """

    try:
        data = yf.Ticker(ticker)
    
    except Exception as e:
        print("Input must be a string.")
        return

    # Check if there is an insufficient amount of data
    # Probably means the ticker is invalid
    if len(data.info) < 100:
        print("Invalid ticker name.")
        return 

    return data.history(period='ytd')['Close'].to_numpy()

# Step 4
def data_prep(data):
    """
    Returns the logs returns of a security. AND the momentum
    """

    rets = data[1:]/np.roll(data,1)[1:]

    momentum = data[10:] - np.roll(data,10)[10:]

    scaler = MinMaxScaler()
    mom_scale = scaler.fit_transform(momentum.reshape(-1,1))

    return np.log(rets)[9:], mom_scale

#Step 5
def stats_table(data):
    """
    Generates simple statistics for the data.
    """
    mean = data.mean()
    var = data.var()
    min = data.min()
    max = data.max()

    return (mean, var, min, max)

#Step 6
def print_table(stats):
    """
    Expects a 4 tuple of mean, var, min, max
    """
    #TODO: Fix f-string
    msg = (
    f"""---------------------------\n
    |  MEAN  | {stats[0]:.2f}  |\n
    |   VAR  | {stats[1]:.2f}  |\n
    |   MIN  | {stats[2]:.2f}  |\n
    |   MAX  | {stats[3]:.2f}  |\n
    --------------------------- \n
    """)

    print(msg)

def sgd_regression(X,y,n_iter=1000,n_save=50):
    """
    """

    X = X.reshape((len(X),1))

    coefs = []
    interps = []

    reg = SGDRegressor()

    for n in range(n_iter):

        reg.partial_fit(X,y)

        if n % n_save == 0:
            coefs.append(reg.coef_[0])
            interps.append(reg.intercept_[0])
    
    return reg, coefs, interps

def make_figure(x, y, interp, coef, title):

    fig = plt.figure()
    plt.scatter(x,y)
    plt.grid()
    vals = np.linspace(x.min(), x.max(), 200)
    pred = interp + vals*coef

    plt.plot(vals, pred, 'r--', linewidth=1.6)
    plt.title(title)

    return fig

# Step 8
def make_gif(x, y, interps, coefs, jumps, save_name):

    images = []
    # This is for clean-up later
    names = []
    for n, (interp, coef) in enumerate(zip(interps, coefs)):
        title = f"Iteration {n*jumps}"
        fname = title + '.png'
        fig = make_figure(x, y, interp, coef, title)
        fig.savefig(fname)
        names.append(fname)
        images.append(imageio.imread(fname))

    imageio.mimsave(save_name, images, duration=0.7)

    for file in names:
        os.remove(file)

def main(ticker, show_table, gif_title):

    tick_data = download_data(ticker)


    log_tick, momentum = data_prep(tick_data)


    if show_table:
        stats_tick = stats_table(tick_data)
        print_table(stats_tick)
    
    reg, coefs, interps = sgd_regression(momentum, log_tick)
    make_gif(momentum, log_tick, interps, coefs, 50, gif_title)  



if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('ticker', help='Ticker name for the target of interest')
    parser.add_argument('-p', '--print-table', default=True, help='Print stats table to stdout')
    parser.add_argument('-o', '--output', help='Name to save gif as.')

    args = parser.parse_args()


    main(args.ticker, args.print_table, args.output)
    print('~~~~~~~~~~~~~~~~~~')
    print('Done')
    print('~~~~~~~~~~~~~~~~~~')
