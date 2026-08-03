POINT_PER_QUIZ = 20


class Score:
    def __init__(self, best_score: int):
        self.best_score = best_score
        self.init()

    def increaseScore(self):
        self.score += POINT_PER_QUIZ
        self.solveQuiz += 1

        if self.score > self.best_score:
            self.newRecord = True

    def getScore(self) -> int:
        return self.score

    def getBestScore(self) -> int:
        return self.best_score

    def getSolveQuizCount(self) -> int:
        return self.solveQuiz

    def findBestScore(self) -> bool:
        if self.newRecord:
            self.best_score = self.score
            self.newRecord = False
            return True
        return False

    def init(self) -> None:
        self.solveQuiz = 0
        self.newRecord = False
        self.score = 0