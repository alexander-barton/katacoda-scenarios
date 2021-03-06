#Imports here

from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import MinMaxScaler
from texttable import Texttable

# Extends the class SGDRegressor() to add stats
class SGDRegressor2(SGDRegressor):
    """
    Extension of the SGDRegressor class from scikit-learn.

    Only adds a method stats(...) that takes predictor data X (without intercept)
    and target data y.

    Calculates an omnibus F-stat, pval and rquared.
    Additionally, calculates standard errors, t-stats, and pvals for all the 
    coefficients in the model (sans intercept).
    """

    def stats(self, X, y):

        n, m = X.shape
        dfe = n - m - 1
        dfm = m
        pred = np.matrix(self.predict(X))

        #Add intercept
        X = np.hstack((np.ones((n,1)),np.matrix(X)))


        #R2 calc
        self.sse_ = np.sum(np.square(y - pred))
        self.sst_ = np.sum(np.square(y - y.mean()))
        self.r2_ = 1 - self.sse_ / self.sst_

        self.Fstat_ = (self.r2_ / (1 - self.r2_)) * (dfe / dfm)
        self.Fpval_ = 1 - sp.stats.f.cdf(self.Fstat_, dfm, dfe)

        self.cov_ = np.cov(X.T)
        self.stand_errors_ = np.sqrt((1/dfe)*(self.sse_/(self.cov_.diagonal()[1:]*dfe+1)))

        # Get t-stats
        self.tstats_ = np.zeros(len(self.stand_errors_))
        self.tstats_ = np.array([self.coef_[n]/se for n, se in enumerate(self.stand_errors_)])


        self.Bpvals_ = 1 - sp.stats.t.cdf(abs(self.tstats_), dfe)




# Step 3
def download_data(ticker):
    """
    Function that downloads 1 month of ticker data
    arguments:
        ticker {str} --- 3-4 character ticker code

    returns:
        data {ndarray - float} --- 1d numpy array of adjusted close prices
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

    return data.history(period='ytd')['Close'].to_numpy().reshape(-1,1)

# Step 4
def data_prep(data):
    """
    Calculates the log returns of a security and the 10 day momentum.

    arguments:
        data {ndarray - float} --- 1d array of data

    returns:
        log returns {ndarray - float} --- 1d array of log returns, truncated to match momentum
        scale momentum {ndarray - float} --- 1d array of 10 day momentum, rescaled using MinMax 

    """


#Step 5
def stats_table(data):
    """
    Calculates simple descriptive statistics for an ndarray.

    arguments:
        data {ndarray - float} --- 
    """

#Step 6
def print_table(mean, var, min, max):
    """
    Prints a table of basic desc. statistics to stdout.  Returns None.
    """
    t = Texttable()
    t.add_rows(
        [["STAT", "VALUE"], ["Mean", mean], ["Var", var], ["Min", min], ["Max", max]]
    )

    print(t.draw())


def print_reg(reg):
    """
    Prints statistical information on a given SGDRegressor2 object.  Returns None.
    """

    t = Texttable()
    
    t.add_rows(
        [ ["STAT", "VAL"], ["F",reg.Fstat_], ["p", reg.Fpval_], ["R2", reg.r2_] ]
    )
    print(t.draw())

    t = Texttable()
    rows = [["Beta", "Coef", "SE", "t", "p"]]
    for n, b in enumerate(reg.coef_):
        rows.append([f"B{n+1}", b, reg.stand_errors_[n], reg.tstats_[n], reg.Bpvals_[n]])
    
    t.add_rows(rows)
    print(t.draw())


def sgd_regression(X, y, n_iter=1000, n_save=50):
    """
    Performs a regression using scikit-learn's SGDRegressor.
    Fits for n_iter iterations and saves the coefficients and intercept every n_save iterations.

    arguments:
        X {ndarray - float} --- an n x m array where n is # samples and m # features
        y {ndarray - float} --- the dependent variable with n samples

    keyword arguments:
        n_iter {int} --- # of iterations of SGD
        n_save {int} --- # of iterations between saving
    
    returns:
        reg {SGDRegressor} --- fitted SGDRegressor object
        coefs {list - float} --- coefficient values during fitting
        interps {list - float} --- intercept values during fitting
    """


def make_figure(x, y, interp, coef, title='Regression', xlabel='', ylabel=''):
    """
    Plots a scatter of x, y and the corresponding regression line interp + coef*range(x)

    arguments:
        x {ndarray - float} --- 1d values to be plotted horizontally
        y {ndarray - float} --- 1d values to be plotted vertically
        inertp {float} --- intercept of the regression
        coef {float} --- coefficient of the regression

    keyword arguments:
        title {str} --- Title for top of the graph
        xlabel {str} ---
        ylabel {str} ---
    
    returns:
        fig {Figure} --- matplotlib Figure, scatter plot with regression line
    """

# Step 8
def make_gif(x, y, interps, coefs, jump_size, save_name='Regression.gif', xlabel='', ylabel=''):
    """

    """
    images = []
    # This is for clean-up later
    names = []
    for n, (interp, coef) in enumerate(zip(interps, coefs)):
        title = f"Iteration {n*jump_size}"
        fname = title + '.png'
        fig = make_figure(x, y, interp, coef, title=title, xlabel=xlabel, ylabel=ylabel)
        fig.savefig(fname)
        names.append(fname)
        images.append(imageio.imread(fname))

    imageio.mimsave(save_name, images, duration=0.7)

    for file in names:
        os.remove(file)

def main():
    """
    Creates a gif of log(rets) ~ momentum for ticker, displays descriptive statistics to stdout.
    """
      



if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('ticker', help='Ticker name for the target of interest')
    parser.add_argument('-p', '--print-table', default=True, help='Print stats table to stdout')
    parser.add_argument('-o', '--output', help='Name to save gif as.')

    args = parser.parse_args()


    main(args.ticker, args.output, show_table=args.print_table)
    print('~~~~~~~~~~~~~~~~~~')
    print(f'{"DONE":^}')
    print('~~~~~~~~~~~~~~~~~~')
