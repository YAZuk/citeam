from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, 'main/index.html', {'latest_question_list': latest_question_list})

def detail_id(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detail(request):
    return render(request, 'main/detail.html', {})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)