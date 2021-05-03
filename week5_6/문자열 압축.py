def solution(s):
    answer = 1001
    
    #문자열 길이가 1인 경우 1 반환
    if len(s) == 1:
        return 1
    # 압축 단위가 중간을 넘어가면 압축이 안됨
    for idx in range(1, len(s)//2 + 1):
        result = ''
        cnt = 1
        
        # 첫 압축 문자
        prev = s[:idx]
        #압축 단위로 for문 순환
        for i in range(idx, len(s)+idx, idx):
            #압축 단위 같은 경우 cnt 증가
            if s[i:i+idx] == prev:
                cnt += 1
            else:
                #cnt가 1이면 숫자 추가 x
                if cnt == 1:
                    cnt = ''
                #압축 문자열에 추가
                result += str(cnt) + prev
                #이전 문자열 변경
                prev = s[i:i+idx]
                #cnt 초기화
                cnt = 1
        #크기 비교
        answer = min(answer, len(result))
    return answer