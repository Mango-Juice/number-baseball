# ===== 라이브러리 ===== #
from random import shuffle


# ===== 상수 ===== #
EASY, HARD, EXIT = ('1', '2', '3')
STRIKE_SCORE, BALL_SCORE = 0.1, 0.05
TRY_LIMIT = 30
EASY_MAX = round(900 * TRY_LIMIT + 30, 2)
HARD_MAX = round(1600 * TRY_LIMIT + 30, 2)


# ===== 클래스 ===== #
class Game:
    # 클래스 생성자
    def __init__(self, n: int) -> None:
        self.n = n # 숫자 자릿수
        self.try_count = self.score = 0 # 시도 횟수, 점수
        
        tmp = list(range(10))
        shuffle(tmp)
        self.answer = tmp[:n] # 정답 숫자


    # 사용자의 입력이 유효한지 판별하는 함수
    def check(self, target: str) -> bool:
        error = ''
        
        try: int(target)
        except: error = '숫자가 아닙니다.'
        if not error and len(target) != self.n: error = f'{self.n}자리가 아닙니다.'
        elif not error and len(target) != len(set(target)): error = '중복 숫자가 있습니다.'

        if error:
            print(error + " 다시 입력해주세요.\n")
            return False
        return True

    
    # 정답과 target을 비교해 스트라이크 및 볼을 판정하는 함수
    def get_count(self, target: str) -> None:
        target = list(map(int, target))
        result = [0, 0]

        for idx, val in enumerate(target):
            if self.answer[idx] == val: result[0] += 1
            elif val in self.answer: result[1] += 1

        return result


    # 사용자의 입력을 바탕으로 스트라이크인지 볼인지 알려준 후 점수를 계산하는 함수
    def play(self, user_input: str) -> bool:
        strike, ball = self.get_count(user_input)

        if strike + ball == 0: print("아웃!!!\n")
        else: print(f"{strike} 스트라이크, {ball} 볼\n")
        
        self.score += STRIKE_SCORE * strike + BALL_SCORE * ball
        self.try_count += 1

        return strike == self.n
            

    # 점수에 시도 점수를 더하는 함수
    def add_final_score(self) -> None:
        self.score += self.n ** 2 * TRY_LIMIT / self.try_count


    # 최종 점수를 프린트하는 함수
    def print_score(self, success: bool) -> None:
        if success: self.add_final_score()
        real_score = round(100 * self.score, 2)
        print(f"최종 점수: {real_score}점")


# ===== 함수 ===== #
def play_baseball(n: int) -> None:
    game = Game(n)

    for i in range(TRY_LIMIT):
        user_input = input(f"0-9로 중복 없이 이루어진 {n}자리 수를 입력해주세요 (포기: -1): ")

        if user_input == "-1":
          print("게임을 포기하셨습니다.")
          game.print_score(False)
          return
        elif not game.check(user_input):
            continue
        elif game.play(user_input):
            print("축하드립니다! 정답을 맞추셨습니다!")
            game.print_score(True)
            return
            
    print("제한 횟수 내에 숫자를 맞추지 못하셨습니다.")
    game.print_score(False)
