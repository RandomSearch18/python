"""Happy Hopper
A sequence of n > 0 integers is called a happy hopper if the absolute values of the
differences between successive elements take on all possible values 1 through n - 1. E.g 1 4 2 3
is a happy hopper because the absolute differences are 3, 2, and 1, respectively. The definition
implies that any sequence of a single integer is a happy hopper. Write a program to
determine whether each of a number of sequences is a happy hopper."""


def is_happy_hopper(numbers: list[int]) -> bool:
    if len(numbers) < 1:
        raise ValueError("Happy hopper check is not valid for empty lists")

    differences = []
    for i in range(0, len(numbers) - 1):
        pair = numbers[i], numbers[i + 1]
        differences.append(abs(pair[0] - pair[1]))

    for required_difference in range(1, len(numbers)):
        if required_difference not in differences:
            return False

    return True


if __name__ == "__main__":
    print(is_happy_hopper([1, 4, 2, 3]))
    print(is_happy_hopper([99]))
    print(is_happy_hopper([99, 999]))
    print(is_happy_hopper([5, 10, 6, 9, 7, 8]))
