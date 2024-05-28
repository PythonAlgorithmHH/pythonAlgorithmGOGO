def solution(arr):
    answer = []

    previous = None

    for number in arr:
        if number != previous:
            answer.append(number)
        previous = number

    return answer
