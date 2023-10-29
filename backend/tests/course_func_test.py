from src.course import add_course, delete_course
from src.database import clear_store
import requests
import pytest

@pytest.fixture
def clear():
    clear_store()


def test_add_course(clear):
    request_data = add_course("COMP3511", "2023-05-31", "2023-08-04", 6)
    assert request_data == {}
    
def test_delete_course(clear):
    request_data = add_course("COMP3511", "2023-05-31", "2023-08-04", 6)
    assert request_data == {}
    request_data = delete_course("COMP3511")
    assert request_data == {}

def test_add_course_no_start(clear):
    request_data = add_course("COMP3511", None, "2023-08-04", 6)
    assert request_data == {}
    
def test_add_course_no_end(clear):
    request_data = add_course("COMP3511", "2023-05-31", None, 6)
    assert request_data == {}
    
def test_add_course_no_uoc(clear):
    request_data = add_course("COMP3511", "2023-05-31", "2023-08-04")
    assert request_data == {}
    
def test_add_course_no_optional_fields(clear):
    request_data = add_course("COMP3511")
    assert request_data == {}
    