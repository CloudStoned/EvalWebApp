from django.contrib import admin
from django.urls import path
from Eval.views import EvaluationsListView, AuthorEvaluationsListView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EvaluationsListView.as_view(), name='home-page'),
    path('author/<str:name>', AuthorEvaluationsListView.as_view(), name='author-posts'),


]   
