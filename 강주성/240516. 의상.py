# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    from collections import defaultdict

    clothes_dict = defaultdict(list)
    for item, category in clothes:
        clothes_dict[category].append(item)

    count = 1
    for category in clothes_dict:
        count *= (len(clothes_dict[category]) + 1)

    return count - 1


# 테스트 케이스
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
