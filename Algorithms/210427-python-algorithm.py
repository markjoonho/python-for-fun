"""
Question Source = https://programmers.co.kr/learn/courses/30/lessons/43165
"""

# ---------------------------------------------------------
# First Solution

import itertools


def solution1(numbers, target):

    lst = []

    for i in numbers:
        lst.append((i, -i))

    p = itertools.product(*lst)
    s = list(map(sum, p))

    return s.count(target)


# ---------------------------------------------------------
# Second Solution!

total = 0


def DFS(numbers, target, sum, pos):
    global total
    if pos >= len(numbers):
        if sum == target:
            total += 1
        return

    DFS(numbers, target, sum + numbers[pos], pos + 1)
    DFS(numbers, target, sum - numbers[pos], pos + 1)


def solution2(numbers, target):
    answer = 0

    DFS(numbers, target, numbers[0], 1)
    DFS(numbers, target, -numbers[0], 1)

    answer = total

    return answer


print(solution2([1, 1, 1, 1], 2))
