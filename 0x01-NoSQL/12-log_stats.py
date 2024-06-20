#!/usr/bin/env python3
"""
Log stats
"""
import pymongo


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    print(f"{mongo_collection.estimated_document_count()} logs")
    print("Methods:")
    print(f"\tmethod GET: {mongo_collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {mongo_collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {mongo_collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {mongo_collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {mongo_collection.count_documents({'method': 'DELETE'})}")
    print(
        f"{mongo_collection.count_documents({'method': 'GET', 'path': '/status'})} status check"
    )


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017')
    logs = client.logs.nginx
    log_stats(logs)
