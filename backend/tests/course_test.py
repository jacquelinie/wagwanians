from src.config import port, url
from src import other
import requests
import pytest

@pytest.fixture
def clear():
    requests.delete(other.CLEAR_URL, json={})


def test_add_course(clear):
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31",
                                                            "end": "2023-08-04", "uoc": 6})
    print(request_data)
    status = request_data.status_code
    assert (status == 200) # Success
    
def test_add_course_already_exist(clear):
    requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31",
                                                            "end": "2023-08-04", "uoc": 6})
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31",
                                                            "end": "2023-08-04", "uoc": 6})
    status = request_data.status_code
    assert (status == 400) # Input Error
    
def test_add_course_no_start(clear):
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511",
                                                            "end": "2023-08-04", "uoc": 6})
    status = request_data.status_code
    assert (status == 200) # Success
    
def test_add_course_no_end(clear):
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31", "uoc": 6})
    status = request_data.status_code
    assert (status == 200) # Success
    
def test_add_course_no_uoc(clear):
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31", "end": "2023-08-04"})
    status = request_data.status_code
    assert (status == 200) # Success
    
def test_add_course_no_optional_fields(clear):
    request_data = requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511"})
    status = request_data.status_code
    assert (status == 200) # Success
    
def test_delete_course(clear):
    requests.post(other.COURSE_ADD_URL, json={'name': "COMP3511", "start": "2023-05-31",
                                                            "end": "2023-08-04", "uoc": 6})
    request_data = requests.delete(other.COURSE_DELETE_URL, json={'name': "COMP3511"})
    status = request_data.status_code
    assert (status == 200) # Success

def test_delete_course_does_not_exist(clear):
    request_data = requests.delete(other.COURSE_DELETE_URL, json={'name': "COMP3511"})
    status = request_data.status_code
    assert (status == 400) # Input Error