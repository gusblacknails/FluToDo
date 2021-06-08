from django.urls import path
from .views import TaskListView, FluTodoLoginView, new_user, TaskDeleteView , TaskCreateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', TaskListView.as_view(), name='Task'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('login/', FluTodoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', new_user, name='signup')
]
