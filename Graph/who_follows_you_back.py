import requests


class GitFollow:
    def load_followers_for(username):
        username_info = requests.get("https://api.github.com/users")
