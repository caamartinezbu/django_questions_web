from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html", {
        "latest_question_list": latest_question_list
        })

    #otra forma mas organizada seria :
    # context = {"latest_question_list": latest_question_list}
    # return render(request, 'polls/index.html', context)
    
    #en rutamiento básico
    #return HttpResponse("<h1>Estas en la pagina principal de la aplicación</H1> ")


def detail(request, question_id):
    #return HttpResponse(f"estas viendo la pregunta numero {question_id}")
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html",{
        "question": question
    })


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html",{
        "question": question
    })
    # return HttpResponse(f"estas viendo los resultados de la pregunta numero {question_id}")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

        

