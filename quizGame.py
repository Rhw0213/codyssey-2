from quiz import Quiz
from IO import IO
from score import Score
import json 
import os

def Game():
    io, quiz_objects, score = Init(readJson())

    while True:
        num = io.print_title()
        match num: 
            case 1:
                solveQuiz(quiz_objects, score, io)


def Init(data):
    quizzes = data["quizzes"]
    best_score = data["best_score"]
    quiz_objects = []

    for d in quizzes:
        quiz = Quiz(d)
        quiz_objects.append(quiz)

    return IO(), quiz_objects, Score(int(best_score)) 

def solveQuiz(quiz_objects: list[Quiz], score: Score, io : IO) -> None:
    index = 0
    while index < len(quiz_objects):
        quiz = quiz_objects[index]

        quiz.print()
        print("선택 ", end="")

        if (quiz.solve(io.inputNum(4))):
            score.increaseScore()
            index += 1
        else:
            io.printResult(score)
            score.init()
            break
        
        io.printLine()
        print()


def readJson():
    with open("state.json", "r", encoding="utf-8") as file:
        return json.load(file)