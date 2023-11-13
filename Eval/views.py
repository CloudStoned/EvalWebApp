from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


from .models import Author, Evaluation, Question, Choice, Answer
from .forms import AnswerForm

from django.views.generic import (
    ListView,DetailView, CreateView, UpdateView, DeleteView
)

from . models import (
    Author,Evaluation,Question,Choice
)

class HomePageListView(ListView):
    model = Evaluation
    template_name = 'home.html'
    context_object_name = 'evaluations'
    # paginated_by = 5

class AuthorEvaluationsListView(ListView):
    model = Evaluation
    template_name = 'partials/author_eval.html'
    context_object_name = 'evaluations'

    def get_queryset(self):
        name = self.kwargs.get('name')
        author = get_object_or_404(Author, name=name)
        return Evaluation.objects.filter(eval_author=author).order_by('-date_created')

class EvaluationListView(ListView):
    model = Evaluation
    template_name = "partials/answer_eval.html"  
    context_object_name = 'evaluations'

def answer_evaluation(request, pk):
    evaluation = get_object_or_404(Evaluation, pk=pk)
    questions = evaluation.question_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # Saving the answers for each question
            for question in questions:
                Answer.objects.create(
                    evaluation=evaluation,
                    question=question,
                    selected_choice=form.cleaned_data['selected_choice'],
                    user=request.user
                )

            # Redirect to the evaluation detail page after submitting answers
            return redirect('eval-detail', pk=pk)
    else:
        form = AnswerForm()

    # Pass additional information to the template
    context = {
        'evaluation': evaluation,
        'questions': questions,
        'form': form,
        'author': evaluation.eval_author,
    }

    return render(request, 'partials/submit_eval.html', context)




