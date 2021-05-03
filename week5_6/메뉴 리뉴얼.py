from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    set_menu = defaultdict(int) #코스요리 
    for menu in orders:
        for i in course:
            tmp = list(combinations(menu, i)) #각 메뉴에 대한 코스요리 조합
            for m in tmp:
                set_menu[''.join(sorted(m))] += 1 #알파벳 정렬 후 튜플 문자열로 합친 후 추가
    
    #이름, 개수 순으로 정렬
    set_menu = sorted(set_menu.items(), key=lambda x: (len(x[0]), -x[1])) 
    
    #초기 설정
    first = set_menu.pop(0)
    #몇 개 요리
    menu_cnt = len(first[0])
    #최소 2명 이상
    if first[1] > 1:
        answer.append(first[0])
        max_cnt = first[1]
    #없을 시 최대값 무한대로 초기화
    else:
        max_cnt = float('inf')

    while(set_menu):
        m = set_menu.pop(0)
        #요리 개수 바뀌는 경우 
        if menu_cnt != len(m[0]):
            menu_cnt = len(m[0])
            #값 초기화
            if m[1] > 1:
                max_cnt = m[1]
                answer.append(m[0])
            #최소 조건 못지킬 시 무한대로 초기화
            else:
                max_cnt = float('inf')
        #요리 개수가 같으며 개수가 최대 개수인 경우
        else:
            if m[1] == max_cnt:
                answer.append(m[0])

    #오름차순 정렬
    answer.sort()
    return answer