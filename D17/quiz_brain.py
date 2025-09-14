from ast import Pass


class QuizBrain:
    def __init__(self,q_bank):
        '''This needs the question bank as an input'''
        self.question_number=0
        self.question_list=q_bank

    def next_question(self):
        current_question=self.question_list[self.question_number]
        #current_question.text()
        user_answer=input(f"Q.{self.question_number:00}: {current_question.question}. (True/False)? ") 
        

