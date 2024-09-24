#binary search in descending list
import time


def location_test(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"



def binary_search(cards, query):
    lo, high = 0, len(cards) - 1

    while lo <= high:
        mid = (lo + high) // 2
        result = location_test(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            lo = mid + 1

    return -1


tests = []

tests.append({
    "input": {
        "cards": [12, 9, 7, 5, 4],
        "query": 7
    },
    "output": 2
})
tests.append({
    "input": {
        "cards": [2],
        "query": 2
    },
    "output": 0
})
tests.append({
    "input": {
        "cards": [10, 6, 8, 7],
        "query": 5
    },
    "output": -1
})

tests.append({
    "input": {
        "cards": [10, 6 ,6, 6, 6, 8, 7],
        "query": 6
    },
    "output": 1
})
print(tests)

for i in range(len(tests)):
    start_time = time.time()
    if binary_search(**tests[i]["input"]) == tests[i]["output"]:
        print("Passed")
    else:
        print("Failed")
    end_time = time.time()
    total_time = start_time - end_time
    print(format(total_time * 1000, ".4f"), "ms")
