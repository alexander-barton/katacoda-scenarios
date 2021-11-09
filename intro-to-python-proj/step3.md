## Data Download

Now let's write a function to download data.  This one is a bit tricky, so it has been provided for you

```
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

    return data.history(period='1mo')['Close'].to_numpy()
```