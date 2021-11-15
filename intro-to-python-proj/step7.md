## Regression

Finally, we will do the regression!

Recall our use of the class `SGDRegressor`.

Here I have provided an updated version called `SGDRegressor2`

Using the `partial_fit()` method of SGDRegressor, perform `n_iter` number of SGD steps.

Save the model coefficient and intercept after every `n_save` steps.

Once you're done, make sure to return the actual regression object as well as the coefficients and intercepts during training.