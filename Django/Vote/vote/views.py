from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.template import loader

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('vote/index.html')
    # context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, request))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'vote/index.html', context)


def detail(request, question_id):
    # return HttpResponse(f"You're looking at question {question_id}.")
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote/detail.html', {'question': question})


def results(request, question_id):
    # return HttpResponse(f"You're looking at the results of question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'vote/results.html', {'question': question})


def votes(request, question_id):
    # return HttpResponse(f"You're voting on question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'vote/detail.html',
                      {'question': question,
                       'error_message': "You didin't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('vote:results', args=(question.id,)))