import pytest
from main import number_from_list_of_digits


def test_with_normal_values():
    assert number_from_list_of_digits([1, 4, 0]) == 140


def test_with_single_input():
    assert number_from_list_of_digits([5]) == 5


def test_with_zero_at_beginning():
    assert number_from_list_of_digits([0, 1, 4]) == 14


def test_with_zeros():
    assert number_from_list_of_digits([0, 0, 0]) == 0


def test_with_zero_in_middle():
    assert number_from_list_of_digits([1, 0, 5]) == 105


def test_with_negative_nums():
    with pytest.raises(ValueError):
        number_from_list_of_digits([-1, -2, -3])


def test_with_invalid_nums():
    with pytest.raises(ValueError):
        number_from_list_of_digits([-1, 10, 12])


def test_with_tuple_input():
    assert number_from_list_of_digits((1, 4, 0)) == 140


def test_with_set_input():
    with pytest.raises(TypeError):
        number_from_list_of_digits({1, 4, 0})


def test_with_iter_input():
    assert number_from_list_of_digits(iter([1, 4, 0])) == 140


def test_with_list_comprehension():
    assert number_from_list_of_digits([x for x in [1, 4, 0]]) == 140


def test_with_bool_inputs():
    with pytest.raises(TypeError):
        number_from_list_of_digits([True, False, True])


def test_with_empty_list():
    with pytest.raises(ValueError):
        number_from_list_of_digits([])


def test_with_string_input():
    with pytest.raises(TypeError):
        number_from_list_of_digits("123")


def test_with_invalid_types():
    with pytest.raises(TypeError):
        number_from_list_of_digits(None)
