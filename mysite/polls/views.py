from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse, HttpResponseRedirect, Http404
from polls.models import *
from django.urls import reverse
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    #lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    #return render(request, template_name, stuff_for_frontend)
    #OR
    context_object_name = 'lastest_question_list'
    template_name = 'polls/index.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

           

class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    
    """ # try:
    #     question = Question.objects.get(pk=question_id)
    #     stuff_for_frontend = {'question':question}
    #     template_name = 'polls/details.html'
        
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # OR
    question = get_object_or_404(Question, pk=question_id)
    stuff_for_frontend = {'question':question}
    template_name = 'polls/details.html'
    return render(request, template_name, stuff_for_frontend) """

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    """ question = get_object_or_404(Question, pk=question_id)
    stuff_for_frontend = {'question':question}
    template_name = 'polls/results.html'
    return render(request, template_name, stuff_for_frontend) """

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form.
        template_name = 'polls/details.html'
        stuff_for_frontend = {'question':question, 'error_message': "You didn't select a choice"}
        return render(request, template_name, stuff_for_frontend)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #always return an HttpResponseRedirect after successfull dealing
        #with POST data. This prevents data from being posted twice if a
        #user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
