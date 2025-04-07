import random


def secret_santa(front, back, alone, seat):
    
    # 앞자리 배정
    for i in range(3, 5):
        for j in range(6):
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
    back.extend(front)
    
    
    '''
    for i in range(2):
        if len(back) == 0:
            num = random.randrange(0, len(alone) + 1)
            alone.remove(num)
        else:
            num = random.randrange(0, len(back) + 1)
            back.remove(num)
        seat[1][i] = num
    back.extend(front)
    '''
    
    
    # 뒷자리 배정
    for i in range(6):
        if len(back) == 0:
            num = alone[random.randrange(0, len(alone))]
            alone.remove(num)
        else:
            num = back[random.randrange(0, len(back))]
            back.remove(num)
        seat[2][i] = num


    for i in range(2):
        if len(back) == 0:
            num = alone[random.randrange(0, len(alone))]
            alone.remove(num)
        else:
            num = back[random.randrange(0, len(back))]
            back.remove(num)
        seat[1][i] = num

    
    
    alone.extend(back)
    
    
    
    
    # 솔로자석 배정
    #print(alone)
    for i in range(2):
        num = alone[random.randrange(0, len(alone))]
        alone.remove(num)
        seat[0][i] = num


    #print(seat)
    return seat




# 배정전 자리
chair = [[0, 0], [0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


# 번호 입력
front_seat = list(map(int,input().split()))
back_seat = list(map(int,input().split()))
alone_seat = list(map(int,input().split()))


#배정된 자리
New_chair = secret_santa(front_seat, back_seat, alone_seat, chair)


# 출력
for i in range(4, 1, -1):
    for j in range(6):
        print(New_chair[i][j], end = " ")
    #print(New_chair[i])
    print()

print(str(New_chair[0][0]) + " X " + str(New_chair[1][0]) + " " + str(New_chair[1][1]) + " X " + str(New_chair[0][1]))

# 예시 입력
'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14
15 16 17 18 19 20
21 22
'''