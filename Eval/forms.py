from django import forms
from . models import (
    Evaluation,Answer
)
from .models import Evaluation, Question, Choice

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['eval_name', 'date_created']
        widgets = {
            'eval_name': forms.TextInput(attrs={'class': 'form-control', 'style':'width: 300px;'}),
            'date_created': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'style':'width: 300px;'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text':forms.TextInput(attrs={'class':'form-control', 'style':'width: 300px;'}),
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text':forms.TextInput(attrs={'class':'form-control', 'style':'width: 300px;'}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'selected_choice']
