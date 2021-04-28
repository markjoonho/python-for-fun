"""
Question Source = https://programmers.co.kr/learn/courses/30/lessons/42578
"""

# Solution!


def solution(clothes):
    answer = 1
    clothes_dict = {}
    for v, k in clothes:
        if k not in clothes_dict:
            clothes_dict[k] = 2
        else:
            clothes_dict[k] += 1

    for cnt in clothes_dict.values():
        answer *= cnt
    return answer - 1


print(
    solution(
        [
            ["yellowhat", "headgear"],
            ["bluesunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
    )
)  # 5

print(
    solution(
        [
            ["crowmask", "face"],
            ["bluesunglasses", "face"],
            ["smoky_makeup", "face"],
        ]
    )
)  # 3
