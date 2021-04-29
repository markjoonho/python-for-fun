"""
Question Source = https://programmers.co.kr/learn/courses/30/lessons/42584
"""

# Solution!


def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for k in range(i + 1, len(prices)):
            if prices[i] <= prices[k]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)

    return answer


print(solution([1, 2, 3, 2, 3]))
