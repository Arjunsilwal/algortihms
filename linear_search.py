"""Alice has some cards with numbers written on them.
She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible.
Write a function to help Bob locate the card."""

import math
import time

#linear Search
def locate_number(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


tests = []

tests.append({
    "input":{
        "cards":[12,9,7,5,4],
        "query": 7
    },
    "output": 2
})
tests.append({
    "input":{
        "cards": [2],
        "query": 2
    },
    "output": 0
})
tests.append({
    "input":{
        "cards": [10,6,8,7],
        "query": 5
    },
    "output": -1
})
print(tests)

for i in range(len(tests)):
    start_time = time.time()
    if locate_number(**tests[i]["input"]) == tests[i]["output"]:
        print("Passed")
    else:
        print("Failed")
    end_time = time.time()
    total_time = start_time - end_time
    print(format(total_time * 1000, ".4f"), "ms")



