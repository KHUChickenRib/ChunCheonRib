def solution(m, n, board):
    answer = 0    
    #알파벳 단위로 원소 저장
    board = [[board[i][j] for j in range(n)] for i in range(m)]
    
    directions = [(0,1), (1,0), (1,1)] #방향
    while True:
        hit = set() #중복 제거 위해 집합 선언
        for i in range(m-1):
            for j in range(n-1):
                flag = True
                if board[i][j] == '-': continue #빈 값은 검사 X
                for direction in directions:
                    #값이 다른 경우 flag False로 변경 후 for문 탈출
                    if board[i][j] != board[i+direction[0]][j+direction[1]]:
                        flag = False
                        break
                if flag: #4개가 일치하는 경우
                    #hit 집합에 저장
                    hit.add((i,j))
                    for direction in directions:
                        hit.add((i+direction[0], j+direction[1]))
        
        #더 이상 맞는 게 없는 경우 while문 탈출
        if len(hit) == 0:
            break
        #맞은 개수 정답에 더해줌
        else:
            answer += len(hit)
            
        #지워진 블록 삭제
        for i,j in hit:
            board[i][j] = '-'
        
        #지워진 블록과 위에 남아있는 블록 위치 변경
        for j in range(0, n):
            tmp = 0
            for i in range(m-1, -1, -1):
                if board[i][j] == '-':
                    tmp += 1
                else:
                    board[i][j],board[i+tmp][j] = board[i+tmp][j],board[i][j]

    return answer