import fin_gif_complete as fg
from sklearn.datasets import load_boston
import pandas as pd

def main(out_name='boston.gif'):

    db = load_boston()
    df = pd.DataFrame(db['data'], columns=db['feature_names'])

    x = df['RM'].values
    y = df['TAX'].values

    print('ROOM STATS')
    fg.print_table(*fg.stats_table(x))

    print('')
    print('TAX STATS')
    fg.print_table(*fg.stats_table(y))

    reg, coefs, interps = fg.sgd_regression(x, y)
    fg.print_reg(reg)
    ffg.make_gif(x, y, interps, coefs, 50, save_name=out_name)

if __name__ == '__main__':

    main()