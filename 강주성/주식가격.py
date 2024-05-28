def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = []

    for i in range(length):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = length - j - 1

    return answer