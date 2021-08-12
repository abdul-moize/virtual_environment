import requests
import numpy
import pandas as pd
import plotext as plt

# requests library exercise
url_posts = 'https://jsonplaceholder.typicode.com/posts'
posts = requests.get(url_posts).json()
url_users = 'https://jsonplaceholder.typicode.com/users'
count = 0
user_id = posts[0]['userId']
for i in posts:
    if i['userId'] == user_id:
        count += 1
# delete posts json array to save space
del posts
users = requests.get(url_users).json()
print('Number of Posts by user: ' + users[user_id-1]['username'] + ' is ' + str(count))

# numpy library exercise
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
