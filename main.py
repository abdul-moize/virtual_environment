from requests_practice import requests_posts
from numpy_practice import numpy_change_values
import numpy
import pandas as pd
import plotext as plt

# requests_posts usage
requests_posts()
# numpy_change_values usage
numpy_change_values()

# pandas exercise
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(numpy.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

# plotext exercise
y = plt.sin(100, 3)
plt.plot(y)
plt.plotsize(100, 30)
plt.title("Plot Example")
plt.show()
