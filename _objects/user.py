# utils
from _utils.string_utils import join_email


# class used to store user information
class User:
    def __init__(self, username, emails, reddit_dict):
        self.username = username
        self.emails = join_email(emails)
        self.subreddits = reddit_dict['subreddits']
        self.reddit_keywords = reddit_dict['keywords']
