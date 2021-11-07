"""
  그냥 만든 숫-자-야-구
"""


# ===== 라이브러리 ===== #
import game


# ===== Main ===== #
if __name__ == "__main__":
  while True:
      if game.start() == game.END: # 사용자가 게임을 종료했을 때
        break