"""
  그냥 만든 숫-자-야-구
"""

import game

while True:
    command = game.get_input()

    if command == game.EASY: game.play_baseball(3)
    elif command == game.HARD: game.play_baseball(4)

    elif command == game.EXIT:
        print("숫자 야구를 종료합니다.")
        break

    else: print("잘못된 명령어입니다. 다시 입력해주세요.")