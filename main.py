from questionmodel import Question
from data import question_data
from quizbrain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
for question in question_bank:
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer, question.answer)

print(f"Você terminou o quiz! Final score: {quiz.score}/{len(question_bank)}")
