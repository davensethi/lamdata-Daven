'I really hope this works '

import pandas  
import numpy


def clean(df):
    df = df.replace(0,np.nan, inplace=True)
    df = df.dropna()
    return df


