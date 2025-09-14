from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]


for a in question_data:
    q=Question(a["text"],a["answer"])
    question_bank.append(q)

#print(question_bank)
quiz=QuizBrain(question_bank)
quiz.next_question()