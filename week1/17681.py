def solution(n, arr1, arr2):
    answer = []
    
    #이진수로 변환하여 저장 / zfill 이용하여 위치 맞춤
    binary_arr1 = [bin(num)[2:].zfill(n) for num in arr1]
    binary_arr2 = [bin(num)[2:].zfill(n) for num in arr2]
    
    
    for i in range(n):
        brick = '' #row 초기화
        for j in range(n):
            #둘 중 하나라도 벽인 경우
            if binary_arr1[i][j] == '1' or binary_arr2[i][j] == '1':
                brick += '#'
            else:
                brick += ' '
        answer.append(brick)
    
    
    return answer