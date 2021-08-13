from requests_practice import requests_posts
from numpy_practice import numpy_change_values
from pandas_practice import pandas_create_custom_df
import plotext as plt

# requests_posts usage
requests_posts()
# numpy_change_values usage
numpy_change_values()
# use module pandas_create_custom_df
pandas_create_custom_df()
# plotext exercise
y = plt.sin(100, 3)
plt.plot(y)
plt.plotsize(100, 30)
plt.title("Plot Example")
plt.show()
