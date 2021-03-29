NOTATION = '0123456789ABCDEF'

#진법 변환 함수
def notation(num, base):
    q,r = divmod(num, base)
    n = NOTATION[r]
    return notation(q,base) + n if q else n

def solution(n, t, m, p):
    answer = ''
    
    str_list = ''
    i = 0
    #정답을 t*m이상 길이만큼 미리 저장
    while len(str_list) < t*m:
        str_list += notation(i, n)
        i += 1
        
    for i in range(t*m):
        if i % m == p - 1: #말해야 하는 숫자 저장
            answer += str_list[i]
            
    return answer