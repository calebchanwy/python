import sys
# <summary >
# During your time at mountain warheouse you will often have to go bug fix your own ( and other peoples!) code.
# The following method should return the smallest value in the given array. If the array is empty then it should return 0.
# However, the last dev has made some bugs.  It seems it only works when the number "1" is the smallest value in the array - for all other cases the method fails
# 4 bugs have been identified within the code.
# See if you can find them all!
# </summary >
# <param name = "numbers" > </param >
# <returns > </returns >


def ReturnSmallestValueInArray(numbers):
    # Bug 1: When given an empty array of numbers, falsely returns a number
    if len(numbers) == 0:
        return 0
    # Bug 2: Initial value of min should be set to maximum, not minimum
    min = sys.maxsize
    for i in range(len(numbers)):
        # Bug 3: Wrong operator used/wrong direction of comparison
        if min > numbers[i]:
            min = numbers[i]
    # Bug 4: Always returned value 1, but should return value at min
    return min
