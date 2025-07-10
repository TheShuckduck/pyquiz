# Example of a quiz file to use from inside the terminal.
# pyquiz.py -- Main starting point of the program.
from quizmanager import QuizManager

class QuizApp:
    QUIZ_FOLDER = "Quizzes"

    def __init__(self):
        self.username = ""
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        # Prints greeting when app starts
        self.greeting()

        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("---------Welcome to PyQuiz!---------")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
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
        print(f"Thank you for playing PyQuiz, {self.username}!")
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
                self.qm.list_quiz()
                print("-------------------------------\n")
                self.menu_header()
                continue
            elif selection[0] == 'T':
                try:
                    quiznum = int(input("Enter quiz number: "))
                    print(f"You have selected {quiznum}.")

                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()

                except:
                    self.menu_error()
                    continue
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
