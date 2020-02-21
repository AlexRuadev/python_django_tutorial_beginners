from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
  # variables name must not change, django convention
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
  # variables name must not change, django convention
  model = Question
  template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'


def vote(request, question_id):
  #  we get the question, or we throw 404 error
  question = get_object_or_404(Question, pk=question_id)
  try:
    # we get the answer for that particular question. request.POST is a dictionnary and we pull out the key choice
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  # we check if the choice doesn't exist or if there's an error
  except (KeyError, Choice.DoesNotExist):
    # if the choice doesn't exist, we return polls/detail.html with the question and an error message.
    return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
    })
  else:
    # increase the selected vote by 1, and save it, and return the url polls:results
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # !!!!!!!!!!!!!!!!!!!!! with POST data. This prevents data from being posted twice if a !!!!!!!!!!!!!!!!!!!
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
