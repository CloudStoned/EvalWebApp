from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,DetailView, CreateView, UpdateView, DeleteView
)

from . models import (
    Author,Evaluation,Question,Choice
)

class EvaluationsListView(ListView):
    model = Evaluation
    template_name = 'home.html'
    context_object_name = 'evaluations'
    # paginated_by = 5

class AuthorEvaluationsListView(ListView):
    model = Evaluation
    template_name = 'partials/author_evals.html'
    context_object_name = 'evaluations'

    def get_queryset(self):
        name = self.kwargs.get('name')
        author = get_object_or_404(Author, name=name)
        return Evaluation.objects.filter(eval_author=author).order_by('-date_created')

    




