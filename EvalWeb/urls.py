from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

from Eval.views import (
    HomePageListView, AuthorEvaluationsListView, EvaluationListView,CreatePageListView, 
    answer_evaluation, create_questions
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageListView.as_view(), name='home-page'),
    path('author/<str:name>/', AuthorEvaluationsListView.as_view(), name='author-posts'),
    path('eval-post/<int:pk>/', EvaluationListView.as_view(), name='eval-detail'),
    path('create-page/', CreatePageListView.as_view(), name = 'create-form'),
    path('answer-post/<int:pk>/', answer_evaluation, name='answer-eval'),
    path('create-eval/', create_questions, name = 'create-questions'),

    #USER VIEWS
    path('register/', user_views.register, name = 'register'),

    # AUTH VIEWS 
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),

]
