## Data Prep

Now we need to write a function to prep the data. 

Assuming we get the data provided for the previous function as our input what should we do?

First we will need to get the log returns of a function.

Hint: `np.log(), np.ravel(1)`

Then we will also need the 10 day momentum

Hint: `data - np.ravel(10)`

Then we will need to scale the momentum data

Hint: `MinMaxScaler()`

And finally, make sure the data are of the appropriate length.  Think about the length of your inputs, and what ravel is doing.