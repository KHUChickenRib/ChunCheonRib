def solution(record):
    answer = []
    dict = {}

    record = [r.split(" ") for r in record]  # 띄어쓰기로 구분

    for row in record:
        # 채팅방 입장 또는 닉네임 변경일 때
        if row[0] == "Enter" or row[0] == "Change":
            dict[row[1]] = row[2]

    for row in record:
        msg = ""
        if row[0] == "Enter":  # 입장인 경우
            msg = f"{dict[row[1]]}님이 들어왔습니다."
        elif row[0] == "Leave":  # 퇴장인 경우
            msg = f"{dict[row[1]]}님이 나갔습니다."
        else:  # 닉네임 변경인 경우
            continue
        answer.append(msg)

    return answer
