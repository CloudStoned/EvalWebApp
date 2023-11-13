from django.contrib import admin
from django.urls import path

from Eval.views import (
    HomePageListView, AuthorEvaluationsListView, EvaluationListView, answer_evaluation
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageListView.as_view(), name='home-page'),
    path('author/<str:name>/', AuthorEvaluationsListView.as_view(), name='author-posts'),
    path('eval-post/<int:pk>/', EvaluationListView.as_view(), name='eval-detail'),
    path('answer-post/<int:pk>/', answer_evaluation, name='answer-eval'),  # Updated this line
]
