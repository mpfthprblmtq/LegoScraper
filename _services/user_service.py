# imports
from os import listdir
from os.path import isfile, join
import json

# _objects
from _objects.user import User


# service class that allows us to keep track of __users within the app
class UserService:

    # __init__
    def __init__(self):
        self.path = './__users/'  # the folder that contains the user files
        self.users = []
        self.init_users()   # init the __users

    # inits the __users
    # scans the __users directory and reads in those text files
    def init_users(self):
        # subscribe to my only_files
        only_files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in only_files:
            # get all the json data in the file
            f = open(self.path + file)
            json_data = json.load(f)
            # extract data into vars
            username = json_data['user_info']['username']
            emails = json_data['user_info']['emails']
            reddit_dict = json_data['reddit']
            self.users.append(User(
                username,
                emails,
                reddit_dict
            ))

    # returns the __users array
    def get_users(self):
        return self.users
