from itertools import combinations


def solution(info, query):
    answer = []
    db = {}
    # 1. info 반복
    # '-' 에 대해 모든 경우의 수 넣어줌
    for i in info:
        temp = i.split()
        con = temp[:-1]  # 점수 제외한 값 : ['java', 'backend', 'junior', 'pizza']  ---> 키
        score = int(temp[-1])  # 150 ---> 값

        for n in range(5):
            combi = list(combinations(range(4), n))
            for c in combi:
                temp_c = con.copy()  # - 포함
                for v in c:  #
                    temp_c[v] = "-"
                change_temp_c = "/".join(temp_c)  # python/-/-/chicken 등등
                if change_temp_c in db:
                    db[change_temp_c].append(score)
                else:
                    db[change_temp_c] = [score]

    # 딕셔너리 값 정렬
    for value in db.values():
        value.sort()

    # 쿼리
    for q in query:
        qry = [
            i for i in q.split() if i != "and"
        ]  # ['java', 'backend', 'junior', 'pizza', '100']
        qry_cnd = "/".join(qry[:-1])  # 점수 제외
        qry_score = int(qry[-1])
        if qry_cnd in db:
            data = db[qry_cnd]
            if len(data) > 0:
                # 이진법
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                # 해당 인덱스 부터 끝까지 개수가 정답
                answer.append(len(data) - start)
        else:
            answer.append(0)
    return answer


"""내 풀이 -> 효율성 통과 x
def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    query = [i.replace('and ','').split() for i in query]
    
    while query:
        q = query.pop(0)
        cnt = 0
        for person in info:
            flag = True
            for i in range(len(q)-1):
                if person[i] != q[i] and q[i] != '-':
                    flag= False
                    break
            if flag:
                if int(person[-1]) >= int(q[-1]):
                    cnt += 1
        answer.append(cnt)
                    
    return answer
    """
