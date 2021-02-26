import pytest
import subprocess
import os
import sys


@pytest.mark.task_0_2
def test_print():
    print(os.path.curdir)
    if os.name in ['Linux', "posix"]:
        task = subprocess.run("python3 src/task_0_2.py", capture_output=True, shell=True)
    else:
        task = subprocess.run("python src/task_0_2.py", capture_output=True, shell=True)
    if task.returncode != 0:
        raise Exception("Ваша программа крашится при запуске!")
        text = task.stderr.decode('utf-8')
        print("Текст ошибки:", text, sep='\n')
    assert task.stdout.decode(encoding='utf-8').strip() == 'For the Alliance!'
