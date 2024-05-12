#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Find things"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    length = logs_collection.count_documents({})
    arr = ["GET", "POST", "PUT", "PATCH", "DELETE"]


    print("{0} logs".format(length))
    print("Methods:")
    for method in arr:
        lengths = logs_collection.count_documents({"method": method})
        print("\tmethod {0}: {1}".format(method, lengths))

    status = logs_collection.count_documents({"method": "GET",
                                            "path": "/status"})
    print("{0} status check".format(status))
