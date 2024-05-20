def solution(phone_book):
    answer = True
    sorted(phone_book,len())

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j]:
                answer = False
    return print(phone_book)
solution(["119", "97674223", "1195524421"])