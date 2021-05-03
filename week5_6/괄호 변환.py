#u, v로 분리
def seperate(p):
    cnt = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        #제일 작은 균형잡힌 괄호가 만들어진 경우
        if cnt == 0:
            return p[:i+1], p[i+1:]

#올바른 괄호 문자열 확인
def balanced(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        #닫힌 괄호가 먼저 나오는 경우    
        if cnt < 0:
            return False
    #올바른 괄호 문자열
    if cnt == 0:
        return True
    #열린 괄호가 남은 경우
    else:
        return False
    
    
def solution(p):
    answer = ''
    #1
    if p == '':
        return ''
    
    #2
    u,v = seperate(p)
    
    #3
    if balanced(u):
        #3-1
        return u + solution(v)
    
    #4
    else:
        #4-1
        answer = '('
        #4-2
        answer += solution(v)
        #4-3
        answer += ')'
        #4-4
        for b in u[1:-1]:
            if b == '(':
                answer += ')'
            else:
                answer += '('
    #4-5
    return answer