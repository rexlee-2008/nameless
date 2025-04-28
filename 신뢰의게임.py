import random
from itertools import combinations

# 점수
payoff_matrix = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1),
}

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
    # move 값은 C,D
    move1 = bot1.move()
    move2 = bot2.move()
    
    bot1.update_history(move1, move2)
    bot2.update_history(move2, move1)
    score1, score2 = payoff_matrix[(move1, move2)]
    bot1.score += score1
    bot2.score += score2

def simulate_match(bot1, bot2, rounds):
    # 여러번을 싸우기 떄문에 다시 싸울떄 전의 기록을 리셋셋
    bot1.reset()
    bot2.reset()
    for _ in range(rounds):
        play_round(bot1, bot2)

def tournament(bots, rounds):
    for bot1, bot2 in combinations(bots, 2):
        print(bot1.name, "VS", bot2.name)
        simulate_match(bot1, bot2, rounds)

# 전략 리스트
strategies = [
    "always_cooperate",
    "always_defect",
    "tit_for_tat",
    "tit_for_two_tats",
    "two_tits_for_tat",
    "random",
    "grim_trigger",
    "pavlov",
    "two_coop_two_defect",
]

# 봇 생성
bots = [Bot(f"Bot{i+1}", strategy) for i, strategy in enumerate(strategies)]

for bot in bots:
    print(bot.name, bot.strategy)

# 토너먼트 실행
rounds = 20
tournament(bots, rounds)

# 결과 출력 (점수 순으로 정렬)
bots_sorted = sorted(bots, key=lambda b: b.score, reverse=True)

print("\n=== 최종 순위 ===")
for rank, bot in enumerate(bots_sorted, 1):
    print(f"{rank}. {bot.name} ({bot.strategy}) - {bot.score}점")

'''

def play_round(bot1, bot2):
    move1 = bot1.move()
    move2 = bot2.move()
    bot1.update_history(move1, move2)
    bot2.update_history(move2, move1)
    return move1, move2

def simulate(bot1_strategy, bot2_strategy, rounds):
    bot1 = Bot(bot1_strategy)
    bot2 = Bot(bot2_strategy)
    results = []
    for _ in range(rounds):
        results.append(play_round(bot1, bot2))
    return results


rounds = 20  # 원하는 횟수 입력
results = simulate("tit_for_tat", "grim_trigger", rounds)

for i, (move1, move2) in enumerate(results):
    print(f"Round {i+1}: Bot1 ({move1}) vs Bot2 ({move2})")

'''

 

'''
항상 협력하는 전략
항상 배신하는 전략
처음엔 협력하고, 이후에는 상대방의 이전 행동을 따라함
상대방이 두 번 연속 배신해야 배신함
상대방이 한 번이라도 배신하면 두 번 연속 배신함
랜덤하게 협력 또는 배신
상대방이 한 번이라도 배신하면 이후에는 계속 배신
이전 라운드에서 같은 선택(협력-협력 or 배신-배신)이었다면 협력, 아니면 배신
2번 협력하고 2번 배신하는 패턴 반복
'''
