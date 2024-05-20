# https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3
def solution(genres, plays):
    from collections import defaultdict

    genre_play_count = defaultdict(int)
    genre_songs = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        genre_songs[genre].append((play, i))


    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)


    result = []


    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        result.extend([song[1] for song in sorted_songs[:2]])

    return result


# 테스트 케이스
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))  # [4, 1, 3, 0]
