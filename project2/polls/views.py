from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect  # Imported by us
from polls.models import *
# Create your views here.


# WRITE A FUNCTION WHICH CAN SEND RESPONSE


# Returns HttpRequest according to request

def hello_world(request):
    return HttpResponse("<marquee><h1>Hello World!</h1></marquee>")  # Constructor of class


def ques_list(request):
    all_ques = Question.objects.all()
    context = {
        'ques_list': all_ques
    }
    return render(request, 'polls/index.html', context)


def ques_detail(request, ques_id):
    all_ques = Question.objects.get(pk=ques_id)
    context = {
        'question_id': ques_id,
        'ques': all_ques,
    }
    return render(request, 'polls/detail.html', context)
    # response = "This is question no: " + str(ques_id)
    # return HttpResponse(response)


def result_detail(request, ques_id):
    ques = Question.objects.get(pk=ques_id)
    context = {
        'this_ques': ques,
    }
    return render(request, 'polls/result.html', context)
    # response = "This is result of ques no " + str(ques_id)
    # return HttpResponse(response)

# get_object_or_404


def vote_detail(request, ques_id):
    ques = Question.objects.get(pk=ques_id)
    choice_pk = request.POST['choice']
    choice_selected = Choice.objects.get(pk=choice_pk)
    choice_selected.no_of_votes += 1
    choice_selected.save()

    return HttpResponseRedirect(reverse("ques_result", kwargs={'ques_id': ques_id}))

    # response = "This is vote of" + str(ques_id)
    # return HttpResponse(response)






