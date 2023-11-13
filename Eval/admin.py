from django.contrib import admin
from .models import Author, Evaluation, Question, Choice, Answer

class EvaluationInLine(admin.TabularInline):
    model = Evaluation

class ChoiceInLine(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

class AuthorAdmin(admin.ModelAdmin):
    inlines = [EvaluationInLine]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

