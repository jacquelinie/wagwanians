"""
Application
Filename: application.py

Author: Jacqueline
Created: 9/8/2023

Description: Contains the server information for
the API routes and swagger API methods
"""

# Imports
import signal
import sys
from json import dumps
from flask import Flask, request, send_from_directory
# from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

# Functions
from src import config
from authentication import auth_login, auth_logout, auth_register, password_reset_request, reset_user_password
from src.course import add_course, delete_course, edit_course_name, edit_course_start, edit_course_end, edit_course_uoc
from src.task import add_task, delete_task, edit_task_name, edit_task_description, edit_task_start_date, edit_task_end_date, set_task_recurring, set_task_unrecurring, check_task, uncheck_task
from src.database import clear_store


# Variables
global course_info
course_info = ["start", "end", "uoc"]


def quit_gracefully(*args):
    sys.exit()


def default_handler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


application = Flask(__name__, static_folder="../static", static_url_path='/static/')


CORS(application)

application.config['TRAP_HTTP_EXCEPTIONS'] = True
application.register_error_handler(Exception, default_handler)


# API Routes
@application.route('/static/<path:path>')
def serve_static_path(path):
    return send_from_directory('', path)


# Methods: GET, POST, PUT, DELETE


@application.route("/clear", methods=['DELETE'])
def handle_clear():
    clear_store()
    return {}


## Authentication

@application.route("/auth/register", methods=['POST'])
def handle_register():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    name_first = request_data['name_first']
    name_last = request_data['name_last']
    return auth_register(email, password, name_first, name_last)


@application.route("/auth/login", methods=['POST'])
def handle_login():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    return auth_login(email, password)


@application.route("/auth/logout", methods=['POST'])
def handle_logout():
    request_data = request.get_json()
    token = request_data['token']
    return auth_logout(token)


@application.route("/auth/passwordreset/request", methods=['POST'])
def handle_reset_request():
    request_data = request.get_json()
    email = request_data['email']
    return password_reset_request(email)


@application.route("/auth/passwordreset/reset", methods=['POST'])
def handle_reset():
    request_data = request.get_json()
    reset_code = str(request_data['reset_code'])
    new_password = str(request_data['new_password'])
    return reset_user_password(reset_code, new_password)



## Course methods

@application.route("/course/add", methods=['POST'])
def handle_course_add():
    request_data = request.get_json()
    name = request_data['name']
    start = request_data.get('start', None)
    end = request_data.get('end', None)
    uoc = request_data.get('uoc', None)
    return add_course(name, start, end, uoc)

@application.route("/course/delete", methods=['DELETE'])
def handle_course_delete():
    request_data = request.get_json()
    name = request_data['name']
    return delete_course(name)

@application.route("/course/edit_name", methods=['PUT'])
def handle_course_edit_name():
    request_data = request.get_json()
    name = request_data['name']
    new_name = request_data['new_name']
    return edit_course_name(name, new_name)

@application.route("/course/edit_start", methods=['PUT'])
def handle_course_edit_start():
    request_data = request.get_json()
    name = request_data['name']
    new_start = request_data['new_start']
    return edit_course_start(name, new_start)

@application.route("/course/edit_end", methods=['PUT'])
def handle_course_edit_end():
    request_data = request.get_json()
    name = request_data['name']
    new_end = request_data['new_end']
    return edit_course_end(name, new_end)

@application.route("/course/edit_uoc", methods=['PUT'])
def handle_course_edit_uoc():
    request_data = request.get_json()
    name = request_data['name']
    new_uoc = request_data['new_uoc']
    return edit_course_uoc(name, new_uoc)


## Task methods

@application.route("/task/add", methods=['POST'])
def handle_task_add():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data.get('name', None)
    description = request_data.get('description', None)
    start_date = request_data.get('start_date', None)
    end_date = request_data.get('end_date', None)
    weighting = request_data.get('weighting', None)
    return add_task(course, name, description, start_date, end_date, weighting)

@application.route("/task/delete", methods=['DELETE'])
def handle_task_delete():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    return delete_task(course, name)

@application.route("/task/edit_name", methods=['PUT'])
def handle_task_edit_task_name():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    new_name = request_data['new_name']
    return edit_task_name(course, name, new_name)

@application.route("/task/edit_description", methods=['PUT'])
def handle_task_edit_description():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    description = request_data['description']
    return edit_task_description(course, name, description)

@application.route("/task/edit_start_date", methods=['PUT'])
def handle_task_edit_start_date():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    start_date = request_data['start_date']
    return edit_task_start_date(course, name, start_date)

@application.route("/task/edit_end_date", methods=['PUT'])
def handle_task_edit_end_date():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    end_date = request_data['end_date']
    return edit_task_end_date(course, name, end_date)

@application.route("/task/set_recurring", methods=['PUT'])
def handle_task_recurring():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    frequency = request_data['frequency']
    return set_task_recurring(course, name, frequency)

@application.route("/task/set_unrecurring", methods=['PUT'])
def handle_task_unrecurring():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    return set_task_unrecurring(course, name)

@application.route("/task/check_task", methods=['PUT'])
def handle_task_check():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    return check_task(course, name)

@application.route("/task/uncheck_task", methods=['PUT'])
def handle_task_uncheck():
    request_data = request.get_json()
    course = request_data['course']
    name = request_data['name']
    return uncheck_task(course, name)







# To run the API server
if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_gracefully)
    application.run(port=config.port)