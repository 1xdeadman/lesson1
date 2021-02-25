import pytest
import src.task_0_1 as task_0_1


@pytest.mark.task_1_2
def test_my_first_variable():
    try:
        assert 'my_first_variable' in dir(task_0_1)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут my_first_variable")
    assert type(task_0_1.my_first_variable) == str
    assert task_0_1.my_first_variable == "well done!"
