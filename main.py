from question_model import Question
from data import question_data
from quiz_brain import QuizBrain, Player

question_bank = []
for x_question in question_data:
    question_bank.append(Question(x_question["text"], x_question["answer"]))

player_name = ''
while player_name == '':
    player_name = input("Hello! What's your name?: ")
    if player_name == '':
        print("Wrong! You should name yourself. Or you can type 'off' to end the game.")
    elif player_name == 'off':
        print("Too sad ;(. Bye!")
        exit()

new_player = Player(player_name)
QuizBrain = QuizBrain(question_bank, new_player)
Global_EndGame = False
while not Global_EndGame:
    QuizBrain.start_the_game()
    TryAgain = input("Wanna try again? [Y, N]: ").lower()
    if TryAgain != "y":
        Global_EndGame = True
