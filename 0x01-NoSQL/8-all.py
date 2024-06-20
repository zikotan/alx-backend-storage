#!/usr/bin/env python3
"""
Retrieve all documents from a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to retrieve documents from.

    Returns:
        list: A list of all documents in the collection.
    """
    return [doc for doc in mongo_collection.find()]
