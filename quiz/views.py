#-*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from weibo import APIClient
from users.LoginRequired import *
from users.models import *
from Http.RequestMethods import *
import random
from datetime import datetime

# Create your views here.
@RequestMethods("GET")
def index(request):
    return render(request,'index.html')

@LoginRequired
@RequestMethods("GET")
def main(request):
    user = request.user
    return render(request, 'main.html', {'profile_url':user.avatar_hd, 'user_name':user.name })

q1_num = 20
q2_num = 5
q3_num = 5

def addquestions(status, level, num):
    questions = Question.objects.filter(level=level).all()
    indexes = randowm.sample(range(len(questions)), num)
    for i in indexes:
        status.questions.add(questions[i])

@LoginRequired
@RequestMethods("GET")
def quiz(request):
   global q1_num, q2_num, q3_num
   total = q1_num + q2_num + q3_num
   quizstatus = reques.user.quizstatus
   if quizstatus.now_qnum == 0:
       addquestions(quizstatus, 1, q1_num)
       addquestions(quizstatus, 2, q2_num)
       addquestions(quizstatus, 3, q3_num)
       quizstatus.save()
   if quizstatus.is_finished == True:
       if quizstatus.now_qnum < total:
           now_question = quizstatus.questions.all()[quizstatus.now_qnum]
           quizstatus.now_qnum += 1
           quizstatus.qtime = datetime.now()
           quizstatus.is_finished = False
           quizstatus.save()
       else:
           history = QuizHistory(user=request.user, qnum=total, rightnum=quizstatus.now_rightnum)
           history.save()
           return render(request, 'finished.html', {'result':history})

   else:
       now_question = quizstatus.questions.all()[quizstatus.now_qnum-1]
   return render(request, 'quiz.html', {'question':now_question})
       

