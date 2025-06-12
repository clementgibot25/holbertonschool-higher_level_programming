#!/usr/bin/python3

"""
Python script to fetch posts from JSONPlaceholder API
"""

import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            pass
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")
