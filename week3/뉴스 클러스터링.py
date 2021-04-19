def solution(str1, str2):
    answer = 0
    
    #대소문자 차이 X -> 모두 소문자로 변경
    str1 = str1.lower()
    str2 = str2.lower()
    
    #각 문자열 집합 만들기
    str1_dict = {}
    str2_dict = {}
    
    tmp = ''
    for i in range(len(str1)-1):
        tmp = str1[i]+str1[i+1]
        if tmp.isalpha(): #문자열인 경우만 추가
            if tmp in str1_dict: #이미 값이 존재하면 개수 +1
                str1_dict[tmp] += 1
            else:
                str1_dict[tmp] = 1
        tmp=''
        
    for i in range(len(str2)-1):
        tmp = str2[i]+str2[i+1]
        if tmp.isalpha():
            if tmp in str2_dict:
                str2_dict[tmp] += 1
            else:
                str2_dict[tmp] = 1
        tmp=''
        
    #모두 공집합인 경우
    if len(str1_dict) == 0 and len(str2_dict) == 0:
        return 65536
    
    #교집합 합집합 구하기
    intersection = 0
    union = 0
    for key, value in str1_dict.items():
        if key in str2_dict:
            intersection += min(value, str2_dict[key]) #교집합은 최소
            union += max(value, str2_dict[key]) #합집합은 최대
            str2_dict[key] = 0 #합집합에 이미 더해졌으므로 0으로 변경
        else:
            union += value
    
    for value in str2_dict.values():
        union += value #나머지 값 합집합에 추가
    
    answer = int((intersection/union)*65536)
    return answer