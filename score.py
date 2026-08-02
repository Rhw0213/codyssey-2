class Score:
    def __init__(self, best_score : int):
        self.score = 0
        self.best_score = best_score

    def increaseScore(self):
        self.score += 20

        if (self.score > self.best_score):
            self.best_score = self.score

    def getScore(self) -> int:
        return self.score

    def getBestScore(self) -> int:
        return self.best_score