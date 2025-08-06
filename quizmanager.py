# QuizManager handles the quiz content

import os.path
import os
import quizparser
import datetime

class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        self.the_quiz = None
        self.quizzes = dict()
        self.results = None
        self.quiztaker = ""

        if (os.path.exists(quizfolder) == False):
            raise FileNotFoundError("Quiz folder doesn't exist!")

        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = os.listdir(self.quizfolder)
        for i, f in enumerate(dircontents):
            filepath = os.path.join(self.quizfolder, f)
            if os.path.isfile(filepath):
                parser = quizparser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(filepath)

    def list_quiz(self):
        for k,v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()

    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)  # Pass the username to Quiz.print_results()

    # save the results of the latest quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass
