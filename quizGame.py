from quiz import Quiz
from IO import IO
import json 

def Game():
    with open("state.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    quizzes = data["quizzes"]
    best_score = data["best_score"]
    quiz_index = 0

    #초기화
    quiz_objects = []

    for d in quizzes:
        quiz = Quiz(d)
        quiz_objects.append(quiz)

    io.print_title();
    #루프
    #while quiz_index <= 4:
    #    quiz = quiz_objects[quiz_index]
    #    quiz_index += 1
    #    quiz.print() 