from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from .models import Tasks
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from django.contrib.auth.models import User
from .forms import NewUserForm
from django.utils.html import strip_tags


class FluTodoLoginView(LoginView):
    template_name = 'register/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


class TaskListView(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = "tasks_list"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def post(self, request):
        input_value = request.POST.get('input')
        input_id = request.POST.get('id')
        current_object = self.model.objects.get(
            id=input_id)
        if input_value == "True":
            current_object.is_completed = False
        else:
            current_object.is_completed = True
        current_object.save()
        context = { "tasks_list": self.model.objects.filter(user=self.request.user) }
        return render(request, 'todo/tasks_list.html', context)

class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('todo/tasks_list.html')

def new_user(request):
    # Creamos el formulario de autenticación vacío
    form = NewUserForm()
  
    def unused_email(email):
        if User.objects.filter(email=email).exists():
            return False
        else:
            return True

    if request.method == "POST":

        # Añadimos los datos recibidos al formulario
        form = NewUserForm(data=request.POST)

        if unused_email(request.POST['email']):
            # Si el formulario es válido...
            if form.is_valid():

                # Creamos la nueva cuenta de usuario
                user = form.save()
                user.email = strip_tags(form.cleaned_data['email'])
                user.username = strip_tags(form.cleaned_data['username'])

                user.save()

                # Si el usuario se crea correctamente
                if user is not None:
                    # Hacemos el login manualmente
                    login(request, user)
                    # Y le redireccionamos a la portada
                    return redirect('/')
            else:
                print('ERROR', form.errors)

        else:
            form.add_error(
                'email', "This email belongs to another user")

    return render(request, 'register/signup.html',  {'form': form})
