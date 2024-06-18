#!/usr/bin/env python3
""" function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs

    Argument:
    mongo_collection: pymongo object
    kwargs: key-value pair
    """
    return mongo_collection.insert_one(kwargs).inserted_id
