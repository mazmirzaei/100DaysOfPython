from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for n in range(0, len(question_data)):
    new_q = Question(question_data[n]['text'], question_data[n]['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print('-------------------------------------------------------------------------------------------')
print("You have  completed the quiz")
print(f"Your total score is {quiz.score}/{quiz.question_number}")







