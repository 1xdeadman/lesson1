import pytest
import subprocess
import src.task_0_3 as task_0_3


@pytest.mark.task_0_3
def test_number():
    try:
        assert 'number' in dir(task_0_3)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут number")
    assert type(task_0_3.number) == int
    assert task_0_3.number == 123


@pytest.mark.task_0_3
def test_second_text():
    try:
        assert 'second_text' in dir(task_0_3)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут number")
    assert type(task_0_3.second_text) == str
    assert task_0_3.second_text == "123"
