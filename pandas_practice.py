"""
this module contains a pandas library example
"""
import numpy
import pandas as pd


def pandas_create_custom_df():
    """
    this function creates a custom dataframe with 
    1. dates('2013-01-01' to '2013-01-06') as 0 column
    2. A, B, C, D as columns
    3. random values
    """
    # pandas exercise
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(numpy.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df)
    