class Score:
    def __init__(self, best_score : int):
        self.score = 0
        self.best_score = best_score
        self.solveQuiz = 0
        self.newRecord = False

    def increaseScore(self):
        self.score += 20
        self.solveQuiz += 1


    def getScore(self) -> int:
        if (self.score > self.best_score):
            #self.best_score = self.score
            #print("🎉 새로운 최고 점수입니다!")
            self.newRecord = True

        return self.score

    def getBestScore(self) -> int:
        return self.best_score 

    def getSolveQuizCount(self) -> int:
        return self.solveQuiz