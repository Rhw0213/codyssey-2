import os

from score import POINT_PER_QUIZ, Score


class IO:
    def isValidNumber(self, enableRange: int, num: int) -> int:
        if num < 1 or num > enableRange:
            print(f"⚠️ 잘못된 입력입니다. 1-{enableRange} 사이의 숫자를 입력하세요.")
            return -1
        return num

    def inputNum(self, enableRange: int, prompt: str = "") -> int:
        """올바른 숫자가 들어올 때까지 다시 입력받는다.

        KeyboardInterrupt / EOFError는 잡지 않고 그대로 올려보내
        게임 쪽에서 저장 후 안전하게 종료하도록 한다.
        """
        while True:
            text = input(prompt).strip()

            if not text:
                print(f"⚠️ 입력이 비어 있습니다. 1-{enableRange} 사이의 숫자를 입력하세요.")
                continue

            try:
                num = int(text)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. 1-{enableRange} 사이의 숫자를 입력하세요.")
                continue

            num = self.isValidNumber(enableRange, num)
            if num != -1:
                return num

    def inputStr(self, words: str) -> str:
        while True:
            text = input(words).strip()
            if text:
                return text
            print("⚠️ 입력이 비어 있습니다. 다시 입력하세요.")

    def print_title(self) -> int:
        print("========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

        num = self.inputNum(5, "선택: ")
        self.clear()
        return num

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def printLine(self):
        print("----------------------------------------")

    def printNewQuiz(self):
        print("📌 새로운 퀴즈를 추가합니다.")
        print()

    def printResult(self, score: Score, total: int):
        print("========================================")
        print(
            f"🏆 결과: {total}문제 중 {score.getSolveQuizCount()}문제 정답! "
            f"({score.getScore()}점)"
        )
        if score.findBestScore():
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")
        print()

    def printHighScore(self, score: Score):
        bestScore = score.getBestScore()

        if bestScore <= 0:
            print("아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어보세요!")
            return

        quizCount = bestScore // POINT_PER_QUIZ
        print(f"🏆 최고 점수: {bestScore}점 ({quizCount}문제 정답)")
