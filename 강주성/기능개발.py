# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        # 현재 기능의 완료 일자를 계산
        days_required = -((p - 100) // s)

        # Q가 비어 있거나, 현재 기능이 새로운 배포 그룹을 시작하는 경우
        if len(Q) == 0 or Q[-1][0] < days_required:
            Q.append([days_required, 1])
        else:
            # 현재 기능이 기존 배포 그룹에 포함되는 경우
            Q[-1][1] += 1

    # 배포 그룹의 크기만 추출하여 반환
    return [q[1] for q in Q]

#못풀었음...