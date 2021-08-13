import numpy


def numpy_change_values():
    numbers = numpy.arange(10)
    # change the even values to 0
    numbers[numbers % 2 == 0] = 0
    print(numbers)
    