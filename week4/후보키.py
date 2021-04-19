from itertools import combinations


def solution(relation):
    row = len(relation)  # 튜플 수
    column = len(relation[0])  # 컬럼 수

    # 전체 조합
    candidates = []
    for i in range(1, column + 1):
        candidates.extend(combinations(range(column), i))

    # 유일성
    unique = []
    for candidate in candidates:  # 조합 인덱스
        tmp = [tuple([item[i] for i in candidate]) for item in relation]  # 조합에 따른 튜플 생성
        if len(set(tmp)) == row:  # 중복이 없을 시 길이가 같음
            unique.append(candidate)  # 인덱스만 저장

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):  # 교집합의 길이와 같은 경우
                answer.discard(unique[j])

    return len(answer)


""" 내 풀이
from itertools import combinations


def solution(relation):
    answer = 0

    row = len(relation)
    column = len(relation[0])

    candidate = []
    for r in relation:
        tmp = []
        for i in range(1, len(r)):
            tmp += combinations(r, i)
        candidate.append(tmp)

    pri_tmp = []
    for j in range(len(candidate[0])):
        tmp = set()
        for i in range(row):
            tmp.add(candidate[i][j])
        pri_tmp.append(tmp)

    pri = []
    for r in pri_tmp:
        if len(r) == row:
            pri.append(r)
            
    return answer
"""
