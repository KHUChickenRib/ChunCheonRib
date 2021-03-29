def solution(dartResult):
    answer = 0
    
    num = ''
    score = []
    for i in dartResult:
        if i == 'S': #Single
            score.append(int(num))
            num = ''
        elif i == 'D': #Double
            score.append(int(num)**2)
            num = ''
        elif i == 'T': #Triple
            score.append(int(num)**3)
            num = ''
            
        elif i == '*': #스타상
            if len(score) < 2: #첫 번째 기회인 경우
                score[-1] *= 2
            else: #그 이외
                score[-1] *= 2
                score[-2] *= 2
        elif i == '#': #아차상
            score[-1] *= -1
                
        else:#점수
            num += i
    
    answer = sum(score)
    
    return answer