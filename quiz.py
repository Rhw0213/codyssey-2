class Quiz:
    def __init__(self, question):
        self.question = question[0]
        self.choices = question[1]
        self.answer = question[2]
    
    def print(self):
        print(self.question)
        for num, choice in enumerate(self.choices, start = 1):
            print(f"{num}. {choice}") 
    
    def solve(self, selectNum):
        if(self.answer == selectNum):
            print("정답입니다.")
        else:
            print("오답입니다.")
            