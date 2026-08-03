class Quiz:
    def __init__(self, quiz):
        # 잘못된 형태의 데이터는 여기서 예외가 발생하고, 호출한 쪽에서 걸러낸다.
        self.question = str(quiz["question"])
        self.choices = [str(choice) for choice in quiz["choices"]]
        self.answer = int(quiz["answer"])

        if not self.question:
            raise ValueError("문제가 비어 있습니다.")
        if len(self.choices) < 2:
            raise ValueError("선택지는 2개 이상이어야 합니다.")
        if not 1 <= self.answer <= len(self.choices):
            raise ValueError("정답 번호가 선택지 범위를 벗어났습니다.")

    def print(self):
        print(self.question)
        print()
        for num, choice in enumerate(self.choices, start=1):
            print(f"{num}. {choice}")
        print()

    def solve(self, selectNum) -> bool:
        if self.answer == selectNum:
            print("✅ 정답입니다!")
            return True

        print(f"❌ 오답입니다. (정답: {self.answer}. {self.choices[self.answer - 1]})")
        return False

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    def printQuestion(self):
        print(f"{self.question}")