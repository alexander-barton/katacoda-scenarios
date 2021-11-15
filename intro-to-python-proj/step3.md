## Data Download

Next we'll examine the `download_data` function.  This is a good time to look at the dogstring.

Docstrings are comments at the beginning of functions that provide a description of what they do, what they need, and what the output.

An example is below:

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
        ...
```