#!/usr/bin/env python3
""" Python function that returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    """
    cursor = mongo_collection.find({"topics": topic}, {"name": 1})
    schools = [school["name"] for school in cursor]
    return schools
