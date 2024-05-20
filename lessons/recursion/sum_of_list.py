def sum(numbers: list[float]):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])


def sum_demo(numbers: list[float]):
    print(f"{numbers} -> {sum(numbers)}")


sum_demo([])
sum_demo([21])
sum_demo([1, 2, 3, 4, 5])
sum_demo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_demo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
