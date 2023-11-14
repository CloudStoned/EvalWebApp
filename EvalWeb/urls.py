from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from Eval.views import (
    HomePageListView, AuthorEvaluationsListView, EvaluationListView,
    create_index, create_eval
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomePageListView.as_view(), name='home-page'),
    path('author/<str:name>/', AuthorEvaluationsListView.as_view(), name='author-posts'),
    path('eval-post/<int:pk>/', EvaluationListView.as_view(), name='eval-detail'),
    path('create-index/', create_index, name = 'create-index'),
    path('create-eval/',create_eval, name = 'create-eval'),
    
    # USER VIEWS
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    # AUTH VIEWS 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
