# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    max = len(nums) // 2
    answer = min(len(set(nums)), max)

    return answer