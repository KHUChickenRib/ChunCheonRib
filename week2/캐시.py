def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities] #도시 이름 모두 소문자로 변환
    
    #캐시가 없는 경우 도시 개수에 5를 곱함
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = []
    #도시를 모두 불러올 때까지
    while cities:
        city = cities.pop(0) #앞에서 도시 하나 가져옴
        
        #캐시 다 차기 전
        if len(cache) < cacheSize:
            #이미 캐시에 존재하는 도시인 경우
            if city in cache:
                cache.pop(cache.index(city)) #캐시 내 동일 도시 제거
                cache.append(city) #캐시 마지막에 다시 추가
                answer += 1 #cache hit이므로 1 더하기
            #캐시에 존재하지 않는 경우
            else:
                cache.append(city) #캐시 마지막에 추가
                answer += 5 #cache miss이므로 5 더하기
                
        #캐시 다 찬 후
        else:
             #이미 캐시에 존재하는 도시인 경우 -> 위 경우와 동일
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            #캐시에 존재하지 않는 경우
            else:
                cache.pop(0) #캐시 제일 앞 도시 제거 -> 그 후 동일
                cache.append(city)
                answer += 5
                
    return answer