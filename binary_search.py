"""Alice has some cards with numbers written on them.
She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given
number by turning over as few cards as possible.
Write a function to help Bob locate the card."""

import math


#linear Search
def locate_card_position(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


tests = []
test1 = {
    "input": {
        "cards": [12, 8, 7, 4, 3, 2],
        "query": 7
    },
    "output": 2
}

tests.append(test1)
result = locate_card_position(**test1["input"])
print(result)
if result == test1["output"]:
    print("result found")
else:
    print("not found")
