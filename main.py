

def number_from_list_of_digits(list_of_digits: list[int]) -> int:
    """
    This function gets a list of int digits, like [1, 4, 0]
    And returns the number made out of the digits, as int (140).
    If there is a problem with input values, raises a ValueError.
    If there is a problem with input types, raises a TypeError.
    """
    output = ""
    for digit in list_of_digits:
        output += str(digit)

    return int(output)


def main() -> None:
    result = number_from_list_of_digits([1, 4, 0])
    print(result)


if __name__ == '__main__':
    main()
