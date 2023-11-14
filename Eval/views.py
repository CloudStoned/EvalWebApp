from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import EvaluationForm,QuestionForm,ChoiceForm
from .models import Author, Evaluation, Question, Choice, Answer

from django.views.generic import ListView

from . models import (
    Author,Evaluation,Question,Choice
)


@method_decorator(login_required, name='dispatch')
class HomePageListView(ListView):
    model = Evaluation
    template_name = 'home.html'
    context_object_name = 'evaluations'
    # paginated_by = 5

@method_decorator(login_required, name='dispatch')
class AuthorEvaluationsListView(ListView):
    model = Evaluation
    template_name = 'partials/author_eval.html'
    context_object_name = 'evaluations'

    def get_queryset(self):
        name = self.kwargs.get('name')
        author = get_object_or_404(Author, name=name)
        return Evaluation.objects.filter(eval_author=author).order_by('-date_created')

@method_decorator(login_required, name='dispatch')
class EvaluationListView(ListView):
    model = Evaluation
    template_name = "partials/answer_eval.html"  
    context_object_name = 'evaluations'


def create_index(request):
    context = {
        'evalForm':EvaluationForm(),
        'questionForm': QuestionForm(),

    }    
    return render(request, 'create_index.html',context)

def create_eval(request):
    if request.method == 'POST':
        pass

    context = {
        'questionForm':QuestionForm(),
        'choiceForm':ChoiceForm()
    }

    return render(request, 'partials/form_eval.html',context)





