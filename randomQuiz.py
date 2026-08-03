import random

from quiz import Quiz


class randomQuiz:
    def rand(self, quizes: list[Quiz]) -> list[Quiz]:
        shuffled_quizzed = quizes.copy()
        random.shuffle(shuffled_quizzed)

        return shuffled_quizzed