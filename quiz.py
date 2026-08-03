class Quiz:
    def __init__(self, quiz):
        self.question = quiz["question"]
        self.choices = quiz["choices"]
        self.answer = quiz["answer"]
    
    def print(self):
        print(self.question)
        for num, choice in enumerate(self.choices, start = 1):
            print(f"{num}. {choice}") 
    
    def solve(self, selectNum) -> bool:
        if(self.answer == selectNum):
            print("정답입니다.")
            return True

        print("오답입니다.")
        return False

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    def printQuestion(self):
        print(f"{self.question}")

            