class Quiz:
    def __init__(self, quiz):
        self.question = quiz["question"]
        self.choices = quiz["choices"]
        self.answer = quiz["answer"]
    
    def print(self):
        print(self.question)
        for num, choice in enumerate(self.choices, start = 1):
            print(f"{num}. {choice}") 
    
    def solve(self, selectNum):
        if(selectNum > len(self.choices) or selectNum < 0):
            return -1;

        if(self.answer == selectNum):
            print("정답입니다.")
        else:
            print("오답입니다.")

        return 1;
            