def solution(msg):
    answer = []
    #사전 정의
    alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    #스택에 알파벳 별로 저장
    msg_stack = [i for i in msg]
    #msg 모두 처리할 때까지
    while msg_stack:
        tmp = msg_stack.pop(0) #제일 앞 알파벳 저장
        
        #사전에 저장된 가장 긴 단어 찾아줌
        while(msg_stack and tmp+msg_stack[0] in alphabet):
            tmp += msg_stack.pop(0)
        
        answer.append(alphabet[tmp]) #사전 색인 번호 저장
        
        #메세지가 남은 경우 사전에 추가
        if msg_stack:
            alphabet[tmp+msg_stack[0]] = len(alphabet) + 1
            
    return answer