'''
Course
Filename: course.py

Author: Jacqueline
Created: 8/8/2023
Description: All functions related to courses.
Allows user to add, delete or edit a course.

'''

from datetime import datetime
from src.database import database, clear_store
from src.error import InputError, AccessError


def add_course(name, start = None, end = None, uoc = None):
    store = database.get()
    courses = store["courses"]

    if name in courses.keys():
        raise InputError("Course already exists")

    # Initiate Course
    course = {}

    initiation = {"start": start, "end": end, "uoc": uoc}
    for k, v in initiation.items():
        if (k == "start" or k == "end") and v != None:
            v = datetime.strptime(v, '%Y-%m-%d').date()
        if k == "uoc" and v != None:
            v = int(v)
        course[k] = v

    course["tasks"] = []
    course["completed"] = False
    courses[name] = course

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}


def delete_course(name):
    store = database.get()
    courses = store["courses"]

    if name not in courses.keys():
        raise InputError("Course does not exist")

    # Remove course
    del courses[name]

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}


def edit_course_name(name, new_name):
    store = database.get()
    courses = store["courses"]

    if name not in courses.keys():
        raise InputError("Course does not exist")

    # Edit name
    course = courses[name]
    del courses[name]
    courses[new_name] = course

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}


def edit_course_start(name, new_start):
    store = database.get()
    courses = store["courses"]

    if name not in courses.keys():
        raise InputError("Course does not exist")
    course = courses[name]

    # Edit start
    course["start"] = datetime.strptime(new_start, '%Y-%m-%d').date()
    courses[name] = course

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}


def edit_course_end(name, new_end):
    store = database.get()
    courses = store["courses"]

    if name not in courses.keys():
        raise InputError("Course does not exist")
    course = courses[name]

    # Edit end
    course["end"] = datetime.strptime(new_end, '%Y-%m-%d').date()
    courses[name] = course

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}


def edit_course_uoc(name, new_uoc):
    store = database.get()
    courses = store["courses"]

    if name not in courses.keys():
        raise InputError("Course does not exist")
    course = courses[name]

    # Edit uoc
    course["uoc"] = int(new_uoc)
    courses[name] = course

    # Set data base
    store["courses"] = courses
    database.set(store)
    return {}

