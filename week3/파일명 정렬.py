def solution(files):
    answer = []
    
    for file in files: #모든 파일명에 대해
        #HEAD 위치 찾기
        for i in range(len(file)):
            if file[i].isdigit():
                break
        head = file[:i] #HEAD 저장

        end = min(i+5, len(file)) #default NUMBER 끝 값
        #NUMBER의 길이가 5 미만인 경우 end 바꿔주기
        for j in range(i, min(i+5,len(file))):
            if not file[j].isdigit():
                end = j
                break

        number = file[i:end] #NUMBER 저장
        tail = file[end:] #TAIL 저장
        
        answer.append([head,number,tail])
    
    #answer를 HEAD, NUMBER순으로 정렬
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    #각 파일명 하나의 문자열로 합쳐주기
    answer = [''.join(ans) for ans in answer]
    return answer