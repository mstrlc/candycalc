from mathlib import divide, add, subtract, multiply, power, sqrt
import cProfile
import fileinput


def calculate_sum(data):
    current_sum = 0
    for number in data:
        current_sum = add(current_sum, number)
    return current_sum


def calculate_arithmetic_mean(total_sum, n):
    return divide(total_sum, n)


def calculate_standard_deviation(data, mean_value, n):
    current_sum = 0
    first_part = divide(1, subtract(n, 1))
    second_part = multiply(n, power(mean_value, 2))
    for number in data:
        third_part = power(number, 2)
        current_sum = add(current_sum, third_part)
    fourth_part = multiply(first_part, subtract(current_sum, second_part))
    return sqrt(fourth_part, 2)


def main():
    data = []
    for line in fileinput.input():
        data.extend([float(x) for x in line.split()])
    total_sum = calculate_sum(data)
    n = len(data)
    arithmetic_mean = calculate_arithmetic_mean(total_sum, n)
    cProfile.run(
        f'calculate_standard_deviation({data}, {arithmetic_mean}, {n})')


if __name__ == '__main__':
    main()
