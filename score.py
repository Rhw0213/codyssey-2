class Score:
    def __init__(self, best_score : int):
        self.best_score = best_score
        self.init()

    def increaseScore(self):
        self.score += 20
        self.solveQuiz += 1

        if (self.score > self.best_score):
            self.newRecord = True 


    def getScore(self) -> int:
        return self.score

    def getBestScore(self) -> int:
        return self.best_score 

    def getSolveQuizCount(self) -> int:
        return self.solveQuiz

    def findBestScore(self) -> bool:
        if(self.newRecord):
            self.best_score = self.score
            return True
        return False

    def init(self) -> None:
        self.solveQuiz = 0
        self.newRecord = False
        self.score = 0