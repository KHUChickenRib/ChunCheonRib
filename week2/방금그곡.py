#테스트 27에 E#도 포함되어 있어서 추가함
change = {'C#' : '1', 'D#' : '2', 'F#' : '3', 'G#' : '4', 'A#' : '5', 'E#' : '6'} 

# #이 포함된 음 하나의 문자로 변경해주는 함수
def change_code(m):
    change_m = ''
    for i in range(len(m)-1): #index range 맞춰주기 위해 길이-1 만큼 진행
        if m[i] == '#': continue #현재 값이 #이면 continue
        if m[i+1] == '#': #지금 문자 뒤에 값이 #이면 위의 딕셔너리를 이용하여 값 변경
            change_m += change[m[i:i+2]]
        else: # #이 안붙는 경우 그대로 저장함
            change_m += m[i]
    if m[-1] != '#': change_m += m[-1] #마지막이 #이 아닌 경우 마지막 문자도 저장
    
    return change_m

def solution(m, musicinfos):
    change_m = change_code(m) #네오가 기억한 멜로디 # 변환하여 저장
                
    m_info = []
    for musicinfo in musicinfos:
        info = musicinfo.split(',') # ,를 기준으로 리스트를 만들어줌
        
        s_h, s_m = map(int,info[0].split(':')) #시작 시와 분 저장
        e_h, e_m = map(int,info[1].split(':')) #종료 시와 분 저장
        play_time = (e_h-s_h)*60 + (e_m-s_m) #재생된 시간 분으로 변환하여 저장
        
        change_score = change_code(info[3]) #악보에서 # 변환하여 저장
        
        code = ''
        for i in range(play_time): #재생 시간만큼 악보 반복 저장
            code += change_score[i%len(change_score)]
        m_info.append([info[2],code]) #새로운 배열에 곡 이름과 재생 시간만큼 반복된 악보 저장
        
    m_info.sort(key=lambda x: -len(x[1])) #재생 시간을 기준으로 내림차순 정렬
    
    for info in m_info:
        if change_m in info[1]: #네오가 기억한 멜로디가 반복된 악보에 포함 될 때 제목 반환
            return info[0]
    return '(None)' #모두 찾은 후 결과가 나오지 않은 경우