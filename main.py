"""
  그냥 만든 숫-자-야-구
"""

import game

while True:
    print("=" * 30)
    print("숫자 야구를 시작합니다.")
    print(f"최고기록: {game.EASY_MAX}점(EASY), {game.HARD_MAX}점(HARD)")
    command = input(f"{game.EASY}: EASY(3자리), {game.HARD}: HARD(4자리), {game.EXIT}: EXIT(종료)\n")

    if command == game.EASY: game.play_baseball(3)
    elif command == game.HARD: game.play_baseball(4)

    elif command == game.EXIT:
        print("숫자 야구를 종료합니다.")
        break

    else: print("잘못된 명령어입니다. 다시 입력해주세요.")