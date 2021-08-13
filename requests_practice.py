import requests


def requests_posts():
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
    print('Number of Posts by user: ' + users[user_id - 1]['username'] + ' is ' + str(count))