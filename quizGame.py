import json

from IO import IO
from quiz import Quiz
from randomQuiz import randomQuiz
from score import Score

SAVE_PATH = "state.json"

# state.json이 없거나 손상되었을 때 사용하는 기본 퀴즈 데이터
DEFAULT_QUIZZES = [
    {
        "question": "Python의 창시자는?",
        "choices": ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],
        "answer": 1,
    },
    {
        "question": "다음 중 변경 가능한(mutable) 자료형은?",
        "choices": ["tuple", "str", "list", "int"],
        "answer": 3,
    },
    {
        "question": "딕셔너리에서 키에 해당하는 값을 안전하게 꺼내는 메서드는?",
        "choices": ["find()", "get()", "search()", "pick()"],
        "answer": 2,
    },
    {
        "question": "클래스의 인스턴스가 만들어질 때 자동으로 호출되는 메서드는?",
        "choices": ["__new__", "__call__", "__init__", "__str__"],
        "answer": 3,
    },
    {
        "question": "JSON 파일을 읽어 파이썬 객체로 바꾸는 함수는?",
        "choices": ["json.dump()", "json.load()", "json.parse()", "json.read()"],
        "answer": 2,
    },
    {
        "question": "예외가 발생해도 프로그램이 멈추지 않도록 감싸는 구문은?",
        "choices": ["if/else", "for/while", "try/except", "with/as"],
        "answer": 3,
    },
]


class QuizGame:
    def __init__(self, save_path: str = SAVE_PATH):
        self.save_path = save_path
        self.io = IO()
        self.rnd = randomQuiz()
        self.quizzes: list[Quiz] = []
        self.score = Score(0)

        self.load()

    # ------------------------------------------------------------------
    # 파일 입출력
    # ------------------------------------------------------------------
    def load(self) -> None:
        data = None

        try:
            with open(self.save_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
        except (json.JSONDecodeError, UnicodeDecodeError):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
        except OSError as error:
            print(f"⚠️ 파일을 읽을 수 없습니다. ({error}) 기본 퀴즈로 시작합니다.")

        self.quizzes, best_score = self.parse(data)
        self.score = Score(best_score)

        print(
            f"📂 퀴즈 {len(self.quizzes)}개, 최고 점수 {best_score}점으로 시작합니다."
        )
        print()

    def parse(self, data) -> tuple[list[Quiz], int]:
        """불러온 데이터를 검증해 Quiz 목록과 최고 점수로 변환한다."""
        quizzes: list[Quiz] = []
        best_score = 0

        if isinstance(data, dict):
            for item in data.get("quizzes", []):
                try:
                    quizzes.append(Quiz(item))
                except (TypeError, KeyError, ValueError, IndexError):
                    print("⚠️ 형식이 잘못된 퀴즈 1개를 건너뛰었습니다.")

            raw_score = data.get("best_score", 0)
            if isinstance(raw_score, int) and raw_score >= 0:
                best_score = raw_score
            else:
                print("⚠️ 최고 점수 값이 올바르지 않아 0으로 초기화합니다.")

        if not quizzes:
            quizzes = [Quiz(item) for item in DEFAULT_QUIZZES]

        return quizzes, best_score

    def save(self) -> bool:
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.score.getBestScore(),
        }

        try:
            with open(self.save_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError as error:
            print(f"⚠️ 저장에 실패했습니다. ({error})")
            return False

        return True

    # ------------------------------------------------------------------
    # 메뉴 흐름
    # ------------------------------------------------------------------
    def run(self) -> None:
        try:
            while True:
                num = self.io.print_title()

                match num:
                    case 1:
                        self.solveQuiz()
                    case 2:
                        self.addQuiz()
                    case 3:
                        self.showQuestions()
                    case 4:
                        self.checkHighScore()
                    case 5:
                        self.save()
                        print("👋 게임을 종료합니다.")
                        return
        except (KeyboardInterrupt, EOFError):
            print()
            print("⚠️ 입력이 중단되었습니다. 저장 후 종료합니다.")
            self.save()

    def solveQuiz(self) -> None:
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            print()
            return

        self.score.init()
        shuffled = self.rnd.rand(self.quizzes)
        total = len(shuffled)

        print(f"📝 퀴즈를 시작합니다! (총 {total}문제)")
        print()

        for index, quiz in enumerate(shuffled, start=1):
            self.io.printLine()
            print(f"[문제 {index}]")
            quiz.print()

            # 틀려도 중간에 끊지 않고 마지막 문제까지 진행한다.
            if quiz.solve(self.io.inputNum(len(quiz.choices), "정답 입력: ")):
                self.score.increaseScore()

            print()

        self.io.printResult(self.score, total)
        self.save()

    def addQuiz(self) -> None:
        self.io.printNewQuiz()

        question = self.io.inputStr("문제를 입력하세요: ")
        choices = [self.io.inputStr(f"선택지 {num}: ") for num in range(1, 5)]
        answer = self.io.inputNum(4, "정답 번호 (1-4): ")

        self.quizzes.append(
            Quiz({"question": question, "choices": choices, "answer": answer})
        )

        # 추가 즉시 저장해서 비정상 종료에도 데이터가 남도록 한다.
        if self.save():
            print("✅ 퀴즈가 추가되었습니다!")
        print()

    def showQuestions(self) -> None:
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            print()
            return

        print(f"📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        self.io.printLine()
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        self.io.printLine()
        print()

    def checkHighScore(self) -> None:
        self.io.printHighScore(self.score)
        print()


def Game():
    """기존 진입점 유지 (내부적으로 QuizGame 클래스를 사용한다)."""
    QuizGame().run()