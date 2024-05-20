# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3
def solution(genres, plays):
    from collections import defaultdict


    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list)

    # 장르별로 총 재생 횟수와 노래 정보를 저장
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        genre_songs[genre].append((play, i))

    # 장르를 총 재생 횟수로 내림차순 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    # 결과를 저장할 리스트
    result = []

    # 장르별로 노래를 재생 횟수로 내림차순, 고유 번호로 오름차순 정렬 후 최대 두 개 추가
    for genre, _ in sorted_genres:
        # 노래를 재생 횟수로 내림차순, 고유 번호로 오름차순 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # 최대 두 개의 노래 선택
        result.extend([song[1] for song in sorted_songs[:2]])

    return result


# 테스트 케이스
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))  # [4, 1, 3, 0]
