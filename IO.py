class IO:
    def isValidNumber(self, enableRange : int, num : int) -> int:
        if (num < 0 or num > enableRange):
            return -1 
        return num 

    def inputNum(self, enableRange : int) -> int:
        num = -1 
        try:
            num = int(input().strip())
        except:
            print("문자는 입력할수 없습니다.")

        return self.isValidNumber(enableRange, num) 

    def print_title(self):
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
            print("선택", end="")

            if (self.inputNum(5) != -1):
                break;

