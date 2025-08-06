# models class to contain the various data models for this program.

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0

    def print_header(self):
        print("\n\n***********************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*************************************************\n")

    def print_results(self):
        print("\n\n***********************************************")

        print("*************************************************\n")

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        self.print_header()
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points

        print("----------------------------------------------------\n")
        return(self.score, self.correct_count, self.total_points)

class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            if len(response) == 0:
                print("Sorry, that is not a valid response. Try again.")
                continue

            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("Sorry, that is not a valid response. Try again.")
                continue

            # Fix: Normalize the correct_answer for comparison
            correct_answer_normalized = self.correct_answer.lower()[0]  # Get first char of correct answer
            if response[0] == correct_answer_normalized:
                self.is_correct = True

            break

class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("Selection? ")

            if len(response) == 0:
                print("Sorry, that is not a valid response. Try again.")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""

