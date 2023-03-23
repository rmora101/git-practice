

def max_value(numbers):
<<<<<<< HEAD
    numbers.sort()
    return numbers[-1]
=======
    """ This function returns the largest number
        in the list.
    """
    max = 0
    for number in numbers: 
        if number > max:
            max = number
    
    return max 
>>>>>>> 43b438d54051313601e02be9d415b32b6a2839e9


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
