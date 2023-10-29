'''
Task
Filename: task.py

Author: Jacqueline
Created: 10/8/2023
Description: All functions related to tasks.
Allows user to add, delete, edit, check and uncheck a task.
Subtask can also be added.

'''

from datetime import datetime
from src.database import database, clear_store
from src.error import InputError, AccessError

def add_task(course_name, name = None, description = None, start_date = datetime.now().strftime('%Y-%m-%d'), end_date = None, weighting = None):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")
    if name == None:
        raise InputError("Name not provided")
    course = courses[course_name]
    task = {}
    task = {"name": name, "description": description, "start_date": datetime.strptime(start_date, '%Y-%m-%d').date(), "end_date": datetime.strptime(end_date, '%Y-%m-%d').date(),
            "weighting": weighting, "recurring": False, "frequency": None, "completed": False}
    course["tasks"].append(task)

    # Update store
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def delete_task(course_name, task_name):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")

    del tasks[task_name]

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def edit_task_name(course_name, task_name, new_task_name):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")

    tasks[new_task_name] = tasks[task_name]
    del tasks[task_name]

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def edit_task_description(course_name, task_name, description):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    task["description"] = description

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def edit_task_start_date(course_name, task_name, start_date):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    task["start_date"] = start_date

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def edit_task_end_date(course_name, task_name, end_date):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    task["end_date"] = end_date

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def set_task_recurring(course_name, task_name, frequency):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    task["recurring"] = True
    task["recurring_frequency"] = frequency

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def set_task_unrecurring(course_name, task_name):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    task["recurring"] = False

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def check_task(course_name, task_name):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    if task["completed"]:
        raise InputError("Task completed already")
    else:
        task["completed"] = True

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


def uncheck_task(course_name, task_name):
    store = database.get()
    courses = store["courses"]

    if course_name not in courses.keys():
        raise InputError("Course not found")

    course = courses[course_name]
    tasks = course["tasks"]
    if task_name not in tasks.keys():
        raise InputError("Task not found")
    task = tasks[task_name]
    if task["completed"]:
        task["completed"] = False
    else:
        raise InputError("Task not completed")

    # Update store
    course["tasks"] = tasks
    courses[course_name] = course
    store["courses"] = courses
    database.set(store)

    return {}


