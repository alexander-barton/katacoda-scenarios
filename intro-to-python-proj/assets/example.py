import fin_gif_complete as fg
import numpy as np
import statsmodels.api as sm
from scipy import stats

def main(out_name='example.gif'):

    x = np.random.normal(0,1,100)
    y = 0.83 + -0.4*x + np.random.normal(0,0.5,100)

    print(type(x))

    print('STATS 1')
    fg.print_table(*fg.stats_table(x))

    print('')
    print('STATS 2')
    fg.print_table(*fg.stats_table(y))

    reg, coefs, interps = fg.sgd_regression(x.reshape(-1,1), y)
    fg.print_reg(reg)
    fg.make_gif(x, y, interps, coefs, 50, save_name=out_name)

    X = sm.add_constant(x)
    model = sm.OLS(y,X)
    results = model.fit()
    print(results.summary())



if __name__ == '__main__':

    main()