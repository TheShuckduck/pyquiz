# Example of a quiz file to use from inside the terminal.
# pyquiz.py -- Main starting point of the program.

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

            if response[0] == self.correct_answer:
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

if __name__ == "__main__":
    qz = Quiz()
    qz.name = "Sample Quiz"
    qz.description = "This is a sample quiz"

    q1 = QuestionTF()
    q1.text = "Broccoli is good for you"
    q1.points = 5
    q1.correct_answer = "t"
    qz.questions.append(q1)

    q2 = QuestionMC()
    q2.text = "What is 2+2?"
    q2.points = 10
    q2.correct_answer = "b"
    ans = Answer()
    ans.name = "a"
    ans.text = "3"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "b"
    ans.text = "4"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "c"
    ans.text = "5"
    q2.answers.append(ans)
    qz.questions.append(q2)

    qz.total_points = q1.points + q2.points
    result = qz.take_quiz()
    print(result)






class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # Prints greeting when app starts
        self.greeting()

        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()

    def greeting(self):
        print("Welcome to PyQuiz!")
        print()

    def menu_header(self):
        print("-------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("Please enter a valid selection:")

    def goodbye(self):
        print("-------------------------------")
        print(f"Thank you for playing PyQUiz, {self.username}!")
        print("-------------------------------")

    def menu(self):
        self.menu_header()
        selection = ""
        while(True):
            selection = input("Selection? ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()

            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("\nAvailable quizzes Are: ")
                # TODO list the quizzes
                print("-------------------------------\n")
                continue
            elif selection[0] == 'T':
                try:
                    quiznum = int(input("Enter quiz number: "))
                    print(f"You have selected {quiznum}.")
                except:
                    self.menu_error()
            else:
                self.menu_error()

    # This is the entry point to the program
    def run(self):
        # Run the startup routine - asks for name, provides welcome message, and so on.
        self.startup()
        # Start the main program menu and run until told to quit
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()