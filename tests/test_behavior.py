import contextlib
import io
import runpy
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
def load(path):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(ROOT / path))

def test_square_and_factorial():
    functions = load('Basic-Syntax/Solution.py')
    assert functions['square'](-3) == 9
    assert functions['square'](0) == 0
    assert functions['factorial'](1) == 1
    assert functions['factorial'](6) == 720

def test_collections_handle_duplicates_and_empty_inputs():
    functions = load('Data-Structures/Solution.py')
    assert set(functions['remove_duplicates']([2, 2, 1])) == {1, 2}
    assert functions['remove_duplicates']([]) == []
    assert functions['find_max']([-5, -2, -9]) == -2
    with pytest.raises(ValueError):
        functions['find_max']([])
    assert functions['reverse_tuple'](('a', 'b', 'c')) == ('c', 'b', 'a')
    assert functions['dict_to_list']({'a':'b'}) == [('a', 'b')]
    assert functions['set_intersection']({1, 2}, {2, 3}) == {2}

def test_student_inherits_person_and_reports_grade(capsys):
    classes = load('Classes/Solution.py')
    student = classes['Student']('Alex', 19, 'B')
    assert isinstance(student, classes['Person'])
    student.introduce()
    student.display_grade()
    assert capsys.readouterr().out == 'My name is Alex and I am 19 years old.\nMy grade is B.\n'
