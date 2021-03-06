
from collections import Counter


def pair_sum(A, goal_sum):
    # Time O(N), Space O(N), where N is the length of the array.
    complementary_count = Counter()
    results = []
    for num in A:
        complementary = goal_sum - num
        if num in complementary_count and complementary_count[num] > 0:
            results.append([num, complementary])
            complementary_count[num] -= 1
        else:
            complementary_count[complementary] += 1
    return results


print(pair_sum([1, 7, 8, 3, 5, 6, 2, 7, 3], 10))


def pair_sum_sort(A, goal_sum):
    # Time O(NlogN), Space O(1), where N is the length of the array.
    A.sort()
    first, last = 0, len(A) - 1
    results = []
    while first < last:
        s = A[first] + A[last]
        if s == goal_sum:
            results.append([A[first], A[last]])
            first += 1
            last -= 1
        elif s < goal_sum:
            first += 1
        else:
            last -= 1
    return results


print(pair_sum_sort([1, 7, 8, 3, 5, 6, 2, 7, 3], 10))
