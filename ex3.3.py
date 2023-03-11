import sys


def reSizeArray():
    nums = []
    prevSize = sys.getsizeof(nums)
    print("inital size of list is:", prevSize)
    numberOfAppendsBeforeResize = 0

    for i in range(63):
        if prevSize != sys.getsizeof(nums):
            print("new size went from ", prevSize, "to ", sys.getsizeof(
                nums), "after ", numberOfAppendsBeforeResize, " iterations")
            prevSize = sys.getsizeof(nums)

        numberOfAppendsBeforeResize += 1

        sys.getsizeof(nums)
        nums.append(i)


reSizeArray()
