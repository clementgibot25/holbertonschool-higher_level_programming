#!/usr/bin/python3

"""
Python script to fetch posts from JSONPlaceholder API
"""


import requests
import csv

def fetch_and_print_posts():
    """
    Fetch and print posts from JSONPlaceholder API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()

posts_prepared = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

with open('posts.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
    writer.writeheader()
    writer.writerows(posts_prepared)

print("Posts saved to posts.csv")
