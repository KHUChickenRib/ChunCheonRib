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