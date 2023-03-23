

def max_value(numbers):
    numbers.sort()
    return numbers[-1]


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
