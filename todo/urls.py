from django.urls import path, include, re_path
from rest_framework import routers
from knox import views as knox_views

from .views import TaskListView, FluTodoLoginView, new_user, TaskDeleteView
from .api.views import LoginAPI, TaskCreateApi, TaskApi, CreateUserAPI, TaskUpdateApi, TaskDeleteApi
from django.contrib.auth.views import LogoutView as UserLogout

router = routers.DefaultRouter()

urlpatterns = [
    path('', TaskListView.as_view(), name='task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('login/', FluTodoLoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(next_page='login'), name='logout'),
    path('signup/', new_user, name='signup'),

    # API

    path('api/',TaskApi.as_view()),
    path('api/create/',TaskCreateApi.as_view(), name='create'),
    path('api/delete/<int:pk>',TaskDeleteApi.as_view(), name='create'),
    path('api/update/<int:pk>',TaskUpdateApi.as_view(), name='update'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', CreateUserAPI.as_view(), name='register'), 
]
