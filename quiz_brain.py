class Player:

    def __init__(self, p_name):
        self.name = p_name
        self.guess_counter = 0
        self.current_answer = ''


class QuizBrain:

    def __init__(self, q_bank, q_player):
        self.question_number = 0
        self.question_list = q_bank
        self.question_list_length = len(q_bank)
        self.cr_player = q_player
        self.end_game = False

    def start_the_game(self):
        self.reset_the_game()
        while not self.check_end_game():
            self.next_question()

    def reset_the_game(self):
        self.set_end_game(False)
        self.reset_player_counter()
        self.reset_question_number()

    def check_last_question(self):
        return self.question_number == self.question_list_length - 1

    def question_list_is_empty(self):
        if self.question_list_length == 0:
            return True
        return False

    def set_end_game(self, value):
        self.end_game = value

    def check_end_game(self):
        if self.end_game:
            print(f"The Game is over. Player: '{self.cr_player.name}' "
                  f"your score is: '{self.cr_player.guess_counter}/{self.question_list_length}'")
            return True
        return False

    def reset_player_counter(self):
        self.cr_player.guess_counter = 0

    def reset_question_number(self):
        self.question_number = 0

    def ask_player_answer(self, current_question):
        current_answer = ''
        while current_answer not in ["true", "false"]:
            current_answer = input(f"Q.{self.question_number + 1} {current_question.text} (True/False)?: ").lower()
        self.cr_player.current_answer = current_answer

    def check_player_answer(self, question):
        if self.cr_player.current_answer == question.answer.lower():
            self.increase_guess_counter()
            self.increase_question_number()
        else:
            print("Wrong answer. Sorry :( ")
            self.set_end_game(True)

    def increase_guess_counter(self):
        self.cr_player.guess_counter += 1

    def increase_question_number(self):
        self.question_number += 1

    def get_question(self):
        return self.question_list[self.question_number]

    def next_question(self):
        if self.question_list_is_empty():
            print("Question list is empty!")
            self.set_end_game(True)
            return
        else:
            if self.check_last_question():
                self.set_end_game(True)
            question = self.get_question()
            self.ask_player_answer(question)
            self.check_player_answer(question)



