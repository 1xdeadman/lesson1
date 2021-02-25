import pytest
import subprocess


@pytest.mark.task_1_3
def test_print():
    task = subprocess.run("python src/task_0_2.py", capture_output=True)
    if task.returncode != 0:
        raise Exception("Ваша программа крашится при запуске!")
        text = task.stderr.decode('utf-8')
        print("Текст ошибки:", text, sep='\n')
    assert task.stdout == b'For the Alliance!\r\n'
