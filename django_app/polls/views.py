from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>estas en la pagina principal de la aplicación</H1> ")


def detail(request, question_id):
    return HttpResponse(f"estas viendo la pregunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"estas votando a la pregunta numero {question_id}")

