#하나만 비교
def compare(target, word):
    for i in range(1, len(target)+1):
        #마지막 인덱스 도착 시
        if i == len(target):
            return i
        #다른 알파벳이 나온 경우
        if target[:i] != word[:i]:
            return i
            
#앞 뒤 비교    
def compare_both(target, word1, word2):
    for i in range(1, len(target)+1):
        #마지막 인덱스 도착 시
        if i == len(target):
            return i
        #둘 다 다른 경우
        if target[:i] != word1[:i] and target[:i] != word2[:i]:
            return i
        
def solution(words):
    answer = 0
    words.sort() #알파벳순 정렬
    
    for idx, word in enumerate(words):
        #맨 앞, 맨 뒤는 하나씩 비교
        if idx == 0:
            answer += compare(word, words[idx+1])
        elif idx == len(words)-1:
            answer += compare(word, words[idx-1])
        #그 외 앞, 뒤 비교
        else:
            answer += compare_both(word, words[idx-1], words[idx+1])
            
    return answer