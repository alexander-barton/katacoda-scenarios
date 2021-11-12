

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

#Step 5
def stats_table(data):
    """
    Generates simple statistics for the data.
    """


#Step 6
def print_table(stats):
    """
    Expects a 4 tuple of mean, var, min, max
    """
# Step 7
def sgd_regression(X, y, n_iter=1000, n_save=50):
    """
    """

# Step 8
def make_figure(x, y, interp, coef, title):
    """
    Plot a figure using matplotlib.
    """

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