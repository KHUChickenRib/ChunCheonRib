def solution(n, t, m, timetable):
    answer = ''
    bus_time = [540 + t*i for i in range(n)] #분으로 변환
    bus_cnt = [0] * len(bus_time) #버스 탑승 인원
    
    timetable.sort() #시간 순 정렬
    latest_time = -1 #가장 늦게 탑승하는 사람 시간
    for t in timetable:
        #분으로 변환
        h, mn = map(int,t.split(':'))
        time = h*60 + mn

        #버스 시간순
        for i in range(len(bus_time)):
            if time <= bus_time[i]: #대기 시간이 버스 도착 시간보다 작거나 같은 경우
                if bus_cnt[i] < m: #탑승가능할 때
                    bus_cnt[i] += 1
                    latest_time = time #가장 늦은 탑승 시간 변경
                    break
    
    #역순으로 확인
    for i in range(len(bus_time)-1,-1,-1):
        #현재 버스 시간보다 뒤에 탑승한 인원이 있는 경우
        if latest_time > bus_time[i]:
            #출력 형식 맞춰주기
            h = str((latest_time-1)//60).zfill(2) #0붙여주기
            mn = str((latest_time-1)%60).zfill(2)
            answer = f'{h}:{mn}'
            break
        #버스 시간에 탑승 가능한 경우
        if bus_cnt[i] < m:
            h = str(bus_time[i]//60).zfill(2)
            mn = str(bus_time[i]%60).zfill(2)
            answer = f'{h}:{mn}'
            break
            
    #탑승시간보다 빨리 타야하는 경우
    if not answer:
            h = str((latest_time-1)//60).zfill(2)
            mn = str((latest_time-1)%60).zfill(2)
            answer = f'{h}:{mn}'
    
    return answer