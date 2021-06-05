from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
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


class TasksListView(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = "tasks_list"


def new_user(request):
    # Creamos el formulario de autenticación vacío
    form = NewUserForm()
    # print("FORM:", form)

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
                    print("USER IS NOT NONE")
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
