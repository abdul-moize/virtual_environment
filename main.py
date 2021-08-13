from requests_practice import requests_posts
import numpy
import pandas as pd
import plotext as plt

# requests_posts usage
requests_posts()
# numpy library
numbers = numpy.arange(10)
# change the even values to 0
numbers[numbers % 2 == 0] = 0
print(numbers)

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
