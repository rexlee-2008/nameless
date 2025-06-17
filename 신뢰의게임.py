import random
#from itertools import combinations

# 점수
# C는 협력, D는 배신
scoreboard = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (0, 0),
}

# 전략별 봇
strategy_list = [
    "tit_for_tat",
    "grim_trigger",
    "always_defect",
    "pavlov",
    "random"
]


class Bot:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
        self.history = []
        self.opponent_history = []
        self.score = 0

    def move(self):
        ## 항상 협력하는 전략
        if self.strategy == "always_cooperate":
            return "C"
        
        ## 항상 배신하는 전략
        elif self.strategy == "always_defect":
            return "D"
        
        ## 처음엔 협력하고, 이후에는 상대방의 이전 행동을 따라함
        elif self.strategy == "tit_for_tat":
            if not self.opponent_history:
                return "C"
            else:
                return self.opponent_history[-1]
        
        ## 상대방이 두 번 연속 배신해야 배신함
        elif self.strategy == "tit_for_two_tats":
            if len(self.opponent_history) < 2:
                return "C"
            elif self.opponent_history[-1] == "D" and self.opponent_history[-2] == "D":
                return "D"
            else:
                return "C"
        
        ## 상대방이 한 번이라도 배신하면 두 번 연속 배신함
        elif self.strategy == "two_tits_for_tat":
            if not self.opponent_history:
                return "C"
            elif self.opponent_history[-1] == "D":
                return "D"
            elif len(self.opponent_history) > 1 and self.opponent_history[-2] == "D":
                return "D"
            else:
                return "C"
        
        ## 랜덤하게 협력 또는 배신
        elif self.strategy == "random":
            return random.choice(["C", "D"])
        
        ## 상대방이 한 번이라도 배신하면 이후에는 계속 배신
        elif self.strategy == "grim_trigger":
            if "D" in self.opponent_history:
                return "D"
            else:
                return "C"
        
        ## 이전 라운드에서 같은 선택(협력-협력 or 배신-배신)이었다면 협력, 아니면 배신
        elif self.strategy == "pavlov":
            if not self.history:
                return "C"
            elif self.history[-1] == "C" and self.opponent_history[-1] == "C":
                return "C"
            elif self.history[-1] == "D" and self.opponent_history[-1] == "D":
                return "C"
            else:
                return "D"
        ## 2번 협력하고 2번 배신하는 패턴 반복
        elif self.strategy == "two_coop_two_defect":
            return "C" if len(self.history) % 4 < 2 else "D"
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")



    def update_history(self, my_move, opponent_move):
        self.history.append(my_move)
        self.opponent_history.append(opponent_move)

    def reset(self):
        self.history.clear()
        self.opponent_history.clear()

def play_round(bot1, bot2):
    move1 = bot1.move()
    move2 = bot2.move()
    
    bot1.update_history(move1, move2)
    bot2.update_history(move2, move1)
    score1, score2 = scoreboard[(move1, move2)]
    bot1.score += score1
    bot2.score += score2

def simulate_match(bot1, bot2, rounds):
    # 봇들의 이전 기록과 점수 초기화
    bot1.reset()
    bot2.reset()
    
    print(f"\n {bot1.name} ({bot1.strategy}) VS {bot2.name} ({bot2.strategy})")
    
    for round_num in range(1, rounds + 1):
        # 각 봇들의 행동
        move1 = bot1.move()
        move2 = bot2.move()
        
        # 각 봇들이 한 행동을 기록후 점수 업데이트
        bot1.update_history(move1, move2)
        bot2.update_history(move2, move1)
        score1, score2 = scoreboard[(move1, move2)]
        bot1.score += score1
        bot2.score += score2
        
        print(f"Round {round_num:02}: {bot1.name} ({move1}) vs {bot2.name} ({move2}) "
              f" 얻은 점수: {score1} - {score2}")

    if bot1.score > bot2.score:
        winner = bot1.name
    elif bot2.score > bot1.score:
        winner = bot2.name
    else:
        winner = "무승부"

    print(f"결과: {bot1.name} {bot1.score}점, {bot2.name} {bot2.score}점  승자: {winner}")

def tournament(strategy_list, rounds):
    # 함수안이라서 밖의 변수와 일치 X
    bots = []
    idx = 1
    
    # 봇 생성
    for strat in strategy_list:
        bots.append(Bot(f"Bot{idx}", strat))
        idx += 1

    # 모든 봇끼리 한 번씩 대결
    for i in range(len(bots)):
        for j in range(i+1, len(bots)):
            simulate_match(bots[i], bots[j], rounds)

    # 결과 정렬해서 출력
    bots_sorted = sorted(bots, key=lambda b: b.score, reverse=True)
    print("\n=== 최종 순위 ===")
    for rank, bot in enumerate(bots_sorted, 1):
        print(f"{rank}. {bot.name} ({bot.strategy}) - {bot.score}점")



'''
def tournament(bots, rounds):
    for bot1, bot2 in combinations(bots, 2):
        simulate_match(bot1, bot2, rounds)
'''

# 봇 생성
bots = []

# 봇 인덱스
idx = 1
for strategy in strategy_list:
    bots.append(Bot(f"Bot{idx}", strategy))
    idx += 1

# 실행 확인
for bot in bots:
    print(f"{bot.name} - {bot.strategy}")

# 토너먼트 실행
rounds = 10
tournament(strategy_list, rounds)