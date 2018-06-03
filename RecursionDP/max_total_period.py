

def max_total_period(A):
    # A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a 15-minute break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment requests (all muliples of 15 minutes, none overlap, and none can be moved), find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.
    # Time O(N), Space O(N), where N is the length of the array.
    def helper(A, start, cache):
        if start >= len(A):
            return 0
        if cache[start] == None:
            best_with = A[start] + helper(A, start+2, cache)
            best_without = helper(A, start+1, cache)
            cache[start] = max(best_with, best_without)
        return cache[start]

    cache = [None] * len(A)
    helper(A, 0, cache)
    return cache[0]


def max_total_iter(A):
    one_away = 0
    two_away = 0
    for i in reversed(range(len(A))):
        best_with = A[i] + two_away
        best_without = one_away
        current = max(best_with, best_without)
        two_away = one_away
        one_away = current
    return one_away


print(max_total_period([30, 15, 60, 75, 45, 15, 15, 45]))
print(max_total_iter([30, 15, 60, 75, 45, 15, 15, 45]))
