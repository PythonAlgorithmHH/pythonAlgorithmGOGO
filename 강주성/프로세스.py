from collections import deque


def solution(priorities, location):
    # 우선순위와 인덱스를 튜플로 묶어서 큐에 저장
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    answer = 0  # 실행 순서를 추적하는 변수

    while queue:
        current = queue.popleft()  # 큐에서 첫 번째 프로세스를 꺼냄

        # 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 있는지 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)  # 우선순위가 높은 프로세스가 있으면 다시 큐에 추가
        else:
            answer += 1  # 현재 프로세스를 실행
            if current[1] == location:  # 현재 프로세스가 우리가 찾고 있는 위치의 프로세스라면
                return answer  # 실행 순서를 반환