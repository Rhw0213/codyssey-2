import os
from score import Score
from quiz import Quiz

class IO:
    def isValidNumber(self, enableRange : int, num : int) -> int:
        if (num < 0 or num > enableRange):
            print("숫자 범위가 맞지 않습니다. 다시 고르세요.")
            return -1 
        return num 

    def inputNum(self, enableRange : int) -> int:
        num = -1 
        try:
            num = int(input().strip())
        except:
            print("문자는 입력할수 없습니다.")

        return self.isValidNumber(enableRange, num) 

    def print_title(self) -> int:
        num = 0

        while True:
            print("========================================")
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("========================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            print("선택 ", end="")

            num = self.inputNum(5)
            if (num != -1):
                os.system("cls" if os.name == "nt" else "clear")
                return num

    def printLine(self):
        print("=========================================")

    def printNewQuiz(self):
        print("새로운 퀴즈를 추가 합니다")

    def printResult(self, score : Score):
        self.printLine()
        print(f"결과: {score.getSolveQuizCount() + 1}문제 중 {score.getSolveQuizCount()}문제 정답!({score.getScore()}점)")
        if (score.findBestScore()):
            print("새로운 최고 점수입니다!")
        self.printLine()

    def inputStr(self, words :str) -> str:
        return input(words).strip()

    def printHighScore(self, score : Score):
        bestScore = score.getBestScore()
        quizCount = bestScore // 20
        print(f"🏆 최고 점수: {bestScore}점 ({quizCount + 1}문제 중 {quizCount}문제 정답)")

