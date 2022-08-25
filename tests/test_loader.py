from matrix_loader.matrix_modification import make_counter_clockwise
import pytest
import os


MATRIX1_RESULT = [10, 50, 90, 130,
                  140, 150, 160, 120,
                  80, 40, 30, 20,
                  60, 100, 110, 70]


MATRIX2_RESULT = [5, 100, 51, 130, 200,
                  201, 202, 203, 204, 205,
                  135, 56, 105, 8, 2,
                  16, 6, 15, 101, 52,
                  131, 132, 133, 134, 55,
                  104, 103, 102, 53, 54]


MATRIX3_RESULT = [1, 5, 9, 13, 17, 21,
                  25, 26, 27, 28, 24, 20,
                  16, 12, 8, 4, 3, 2,
                  6, 10, 14, 18, 22, 23,
                  19, 15, 11, 7]


MATRIX4_RESULT = [1, 5, 6, 2]


def get_fixture_path(name):
    return os.path.join('tests/fixtures', name)


@pytest.mark.parametrize(
    'input_file_name, expected_result',
    [('matrix1_before.txt', MATRIX1_RESULT),
    ('matrix2_before.txt', MATRIX2_RESULT),
    ('matrix3_before.txt', MATRIX3_RESULT),
    ('matrix4_before.txt', MATRIX4_RESULT)])
def test_matrix(input_file_name, expected_result):
    file = get_fixture_path(input_file_name)
    input_matrix = ''
    with open(file) as read_file:
        for line in read_file:
            input_matrix += line
    output = make_counter_clockwise(input_matrix)
    assert output == expected_result
