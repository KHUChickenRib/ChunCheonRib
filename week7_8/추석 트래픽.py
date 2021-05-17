def trafic(time, lst):
    c = 0
    start = time
    end = time + 1000
    for i in lst:
        if i[1] >= start and i[0] < end:
            c += 1
    return c

def solution(lines):
    answer = 0
    lst = []
    for line in lines:
        day, time, work = line.split()
        h,m,s = time.split(':')
        end = int(h)*3600 + int(m)+60 + float(s)+1000
        start = end - float(work[:-1])*1000 + 1
        lst.append([start, end])

        for i in lst:
            answer = max(answer,trafic(i[0],lst),trafic(i[1],lst)) 

    return answer