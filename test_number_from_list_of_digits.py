import pytest
from main import number_from_list_of_digits


def test_with_normal_values():
    assert number_from_list_of_digits([1, 4, 0]) == 140


pytest.main()
