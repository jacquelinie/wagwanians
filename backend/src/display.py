'''
Display
Filename: display.py

Author: Jacqueline
Created: 9/8/2023
Description: All functions relate to the front end of the application.

'''

from src.database import database

def get_courses_name():
    store = database.get()
    courses = store["courses"]
    course_names = courses.keys()

    return { "course_names": course_names }

def get_courses():
    store = database.get()
    courses = store["courses"]

    return { "courses": courses }

def get_tasks(course_name):
    store = database.get()
    courses = store["courses"]
    course = courses[course_name]
    tasks = course["tasks"]

    return { "tasks": tasks }

