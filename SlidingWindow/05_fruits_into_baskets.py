"""
Given an array of characters where each character represents a fruit tree, you are 
given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one 
type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., 
you will stop when you have to pick from a third fruit type.
"""


def fruits_into_baskets(fruits: list):
    baskets = {}
    start, result = 0, 0

    for i, c in enumerate(fruits):
        baskets[c] = baskets.get(c, 0) + 1

        while len(baskets) > 2:
            start_char = fruits[start]
            baskets[start_char] -= 1
            start += 1
            if baskets[start_char] == 0:
                del baskets[start_char]

        result = max(i - start + 1, result)

    return result


if __name__ == '__main__':
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
