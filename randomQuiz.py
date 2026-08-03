from quiz import Quiz
import random  

class randomQuiz:

    def rand(self, quizes : list[Quiz]):
        shuffled_quizzed = quizes.copy()
        random.shuffle(shuffled_quizzed)

        return shuffled_quizzed


