from django import forms
from . models import (
    Author,Evaluation,Question,Choice,Answer
)

class AuthorNameForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'name',
        )

class EvaluaionForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = (
            "eval_name",
            "date_created"
        )

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            "question_text",
        )

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = (
            "choice_text",
            "answers"
        )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'selected_choice']
