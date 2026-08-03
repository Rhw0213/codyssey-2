from quiz import Quiz
from IO import IO
from score import Score
import json 
import os
import sys
from randomQuiz import randomQuiz 

def Game():
    data = readJson()
    io, quiz_objects, score = Init(data)

    while True:
        num = io.print_title()
        match num: 
            case 1:
                solveQuiz(quiz_objects, score, io)
            case 2:
                addQuiz(quiz_objects, io)
            case 3:
                showQuestions(quiz_objects)
            case 4:
                checkHighScore(score, io)
            case 5:
                saveJson(data, score, quiz_objects)
                sys.exit(0)


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

    rnd = randomQuiz() 

    shuffleQuizs = rnd.rand(quiz_objects)
    
    while index < len(shuffleQuizs):
        quiz = shuffleQuizs[index]

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

def saveJson(data, score : Score, quiz_objects : list[Quiz]):
    quiz_data = []

    for quiz in quiz_objects:
        quiz_data.append(quiz.to_dict())

        newData = {
            "quizzes" : quiz_data,
            "best_score" : score.getBestScore()
        }

    with open("state.json", "w", encoding="utf-8") as file:
        json.dump(newData, file, ensure_ascii=False, indent=4)

def addQuiz(quiz_objects: list[Quiz], io: IO) -> None:
    io.printNewQuiz()
    question = io.inputStr("문제를 입력하세요")

    choices = []

    for num in range(1, 5):
        choice = io.inputStr(f"선택지 {num} ")
        choices.append(choice)

    print("정답 : ", end = "")
    answer = io.inputNum(4)

    quiz_data = {
        "question": question,
        "choices": choices,
        "answer": answer 
    }

    new_Quiz =  Quiz(quiz_data)
    quiz_objects.append(new_Quiz)

def checkHighScore(score : Score, io : IO):
    io.printHighScore(score)

def showQuestions(quiz_object: list[Quiz]):
    for index, quiz in enumerate(quiz_object, start=1):
        print(f"[{index}] {quiz.question}")
        
