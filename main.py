from typing import Iterable

def number_from_list_of_digits(list_of_digits: Iterable[int]) -> int:
    """
    This function gets a list of int digits, like [1, 4, 0]
    And returns the number made out of the digits, as int (140).
    If there is a problem with input values, raises a ValueError.
    If there is a problem with input types, raises a TypeError.
    """
    if isinstance(list_of_digits, set):
        raise TypeError("Unable to create a number, as sets are unordered.")

    output = ""
    for digit in list_of_digits:
        if 0 < digit >= 10:
            raise ValueError("Only digits between 0-9 allowed.")
        elif isinstance(digit, bool):
            raise TypeError("Only digits between 0-9 allowed.")

        output += str(int(digit))

    return int(output)


def main() -> None:
    result = number_from_list_of_digits([1, 4, 0])
    print(result)


if __name__ == '__main__':
    main()
