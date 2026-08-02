from quiz import Quiz

def main():
    quiz = Quiz(["문제 : ", 
                 ["정답1", "정답2", "정답3", "정답4"], 
                 4])

    quiz.print()

if __name__ == "__main__":
    main()
