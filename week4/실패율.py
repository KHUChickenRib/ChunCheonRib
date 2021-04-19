def solution(N, stages):
    answer = []
    # 스테이지별 딕셔너리 선언
    stage_user = {}
    for i in range(1, N + 1):
        stage_user[i] = 0

    # 스테이지에 있는 사용자수 저장
    for stage in stages:
        if stage == N + 1:
            continue
        stage_user[stage] += 1

    player = len(stages)  # 총 사용자수

    for key, value in stage_user.items():
        if player == 0:  # 도달한 유저가 없는 경우
            stage_user[key] = 0
        else:  # 실패율 계산
            stage_user[key] = value / player
        player -= value  # 스테이지에 도달한 유저 계산

    result = sorted(stage_user.items(), key=lambda x: -x[1])  # 실패율 내림차순 정렬
    answer = [i[0] for i in result]  # 스테이지만 저장

    return answer
