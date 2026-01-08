import pytest

def test_equal_or_not_equal():
    assert 3==3
    assert 3!=1

def test_is_instance():
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)

def test_boolean():
    validate = True
    assert validate is True
    assert ('hello' == 'state') is False

def test_type():
    assert type('hello' is str)
    assert type('war' is not int)

def test_greater_or_less_than():
    assert 7 > 3
    assert 3 < 7

def test_list():
    num = [1, 2, 3, 4]
    any_l = [False, False]
    assert 1 in num
    assert 's' not in num
    assert all(num)
    assert not any(any_l)


class Student:
    def __init__(self, first_name: str, last_name:str, major: str, years: str):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_stu():
     return Student('saa', 'ni', 'cs', 1)


def test_student_init(default_stu):
    assert default_stu.first_name == 'saa', 'first name should be s'
    assert default_stu.last_name == 'ni', 'last name should be ni'
    assert default_stu.major == 'cs'
    assert default_stu.years == 1


    