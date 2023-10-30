'''
Database
Filename: database.py

Author: Jacqueline
Created: 8/8/2023

Description:
This contains a definition for a Database class which you should use to store your data.
You don't need to understand how it works at this point, just how to use it :)

The database variable is global, meaning that so long as you import it into any
python file in src, you can access its contents.

'''

import pickle
FILE_LOCATION = "database.p"

initial_object = {
    'users': {},
    'courses': {},
} 

def clear_store():
    store = database.get()
    store["courses"] = {}
    database.set(store)

def pickle_and_store(object_to_persist: dict):
    with open(FILE_LOCATION, "wb") as file:
        pickle.dump(object_to_persist, file)


def unpickle_and_load() -> dict:
    data_contents = {}
    with open(FILE_LOCATION, "rb") as file:
        data_contents = pickle.load(file)

    # When authentication is added, clear user sessions
    # for user in data_contents['users'].values():
    #     user['sessions'] = []

    return data_contents


class Database:
    def __init__(self):
        try:
            self.__store = unpickle_and_load()
        except:
            self.__store = initial_object

    def get(self):
        return self.__store

    def set(self, store):
        if not isinstance(store, dict):
            raise TypeError('store must be of type dictionary')
        self.__store = store
        pickle_and_store(self.__store)


global database
database = Database()
