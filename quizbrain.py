class QuizBrain:
    def __init__(self, question_list):
      self.question_number = 0
      self.question_list = question_list
      self.score = 0

    def next_question(self):
      current_question = self.question_list[self.question_number]
      self.question_number += 1
      return input(f"Q.{self.question_number}:{current_question.text} (True/False): ")

    def check_answer(self, user_answer, correct_answer):
      self.user_answer = user_answer
      self.correct_answer = correct_answer
      if self.user_answer.lower() == self.correct_answer.lower():
        self.score += 1
        print("Você acertou!")
      else:
        print("Errado!")
      print(f"A resposta era: {self.correct_answer}. Score: {self.score}/{len(self.question_list)}\n")
