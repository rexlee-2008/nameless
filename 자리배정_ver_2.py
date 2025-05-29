import random


def secret_santa(front, back, alone, seat):
    
    # 중앙좌석 배정
    for i in range(4):
        for j in range(4):
            if len(front) == 0:
                if len(back) == 0:
                    num = alone[random.randrange(0, len(alone))]
                    alone.remove(num)
                else:
                    num = back[random.randrange(0, len(back))]
                    back.remove(num)
            else:
                num = front[random.randrange(0, len(front))]
                #print(front, num)
                front.remove(num)
            seat[i][j] = num
    #back.extend(front)
    print(front, back, alone)
    
    
    # 솔로좌석 배정
    print(alone)
    for i in range(6):
        num = alone[random.randrange(0, len(alone))]
        alone.remove(num)
        seat[4][i] = num


    print(seat)
    return seat




# 배치모양
#chair = [[0, 0], [0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
chair = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, "X", "X"]]


# 번호 입력
front_seat = list(map(int,input().split()))
back_seat = list(map(int,input().split()))
alone_seat = list(map(int,input().split()))


# 배정된 자리 저장
New_chair = secret_santa(front_seat, back_seat, alone_seat, chair)


# 출력
for i in range(4):
    if i == 3:
        print("X", end = " ")
    else:
        print(New_chair[4][i], end = " ")
    for j in range(4):

        if j % 2 == 0 or j == 0:
            print(New_chair[i][j], end = "+")
        else:
            print(New_chair[i][j], end = " ")

    if i == 3:
        print("X", end = " ")
    else:
        print(New_chair[4][5 - i], end = " ")
    #print(New_chair[i])
    print()


# 예시 입력
'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14
15 16 17 18 19 20
21 22

1 2 3 4 5 6 7 8 9 10 11 12 13 14
15 16
17 18 19 20 21 22
'''