from django.urls import path
from .views import TasksListView, FluTodoLoginView, new_user
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', TasksListView.as_view(), name='Tasks'),
    path('login/', FluTodoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', new_user, name='signup')
]
