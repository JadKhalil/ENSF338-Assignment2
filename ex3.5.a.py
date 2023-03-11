import random
import timeit
import time
import matplotlib.pyplot as plt
#  inefficent implementation
# just a linear search
# worst case search is O(n)


def LinearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            found = True
            break

    if found:
        return True
    return False

# efficent implementation uses the fact that it is sorted to reduce the time complexity
# time complexity become logarithmic base 2
# worst case is O(log(n))


def BinarySearch(nums, target):
    lo = 0
    hi = len(nums)-1
    found = False

    while lo <= hi:
        mid = lo + ((hi-lo) // 2)
        if nums[mid] == target:
            found = True
            break
        elif nums[mid] > target:
            hi = lo-1
        else:
            lo = hi+1
    if found:
        return True
    return False


def PlotResults(lSearch, bSearch):

    xPoints = [i for i in range(len(bSearch))]

    plt.subplot(1, 2, 1)
    plt.plot(xPoints, lSearch)
    plt.title("Linear Search")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.subplot(1, 2, 2)
    plt.plot(xPoints, bSearch)
    plt.title("Binary Search")
    plt.xlabel('iteration number')
    plt.ylabel('function call speed')

    plt.show()


if __name__ == "__main__":
    randomlist = [random.randint(0, 100) for _ in range(1000)]
    randomInt = random.randint(0, 100)

    linearSearchTime = []
    BinarySearchTime = []
    for i in range(100):
        BinarySearchTime.append(timeit.timeit(stmt='BinarySearch(randomlist, randomInt)', setup='', timer=time.perf_counter,
                                              number=1, globals=globals()))

    for i in range(100):
        linearSearchTime.append(timeit.timeit(stmt='LinearSearch(randomlist, randomInt)', setup='', timer=time.perf_counter,
                                              number=1, globals=globals()))

    PlotResults(linearSearchTime, BinarySearchTime)

    # Timing of both
    # print(linearSearchTime)
    # print(BinarySearchTime)
