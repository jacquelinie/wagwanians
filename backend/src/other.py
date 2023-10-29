"""
Other
Filename: other.py

Author: Jacqueline
Created: 9/8/2023

Description: Contains the URLs of the API routes
"""

from src.config import url

CLEAR_URL = f"{url}/clear"

COURSE_ADD_URL = f"{url}/course/add"
COURSE_DELETE_URL = f"{url}/course/delete"
COURSE_EDIT_NAME_URL = f"{url}/course/edit_name"
COURSE_EDIT_START_URL = f"{url}/course/edit_start"
COURSE_EDIT_END_URL = f"{url}/course/edit_end"
COURSE_EDIT_UOC_URL = f"{url}/course/edit_uoc"

TASK_ADD_URL = f"{url}/task/add"
TASK_DELETE_URL = f"{url}/task/delete"
TASK_EDIT_NAME_URL = f"{url}/task/edit_name" 
TASK_EDIT_DESCRIPTION_URL = f"{url}/task/edit_description"
TASK_EDIT_START_DATE_URL = f"{url}/task/edit_start_date"
TASK_EDIT_END_DATE_URL = f"{url}/task/edit_end_date"
TASK_SET_RECURRING_URL = f"{url}/task/set_recurring"
TASK_SET_UNRECURRING_URL = f"{url}/task/set_unrecurring"
TASK_CHECK_TASK_URL = f"{url}/task/check_task"
TASK_UNCHECK_TASK_URL = f"{url}/task/uncheck_task"

