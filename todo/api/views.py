from django.contrib.auth import  login
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import TaskSerializer, UserSerializer, RegisterSerializer
from todo.models import Task

# login / logout

from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # line above create session based authentication with token based authentication.
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



#  create user

class CreateUserAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
# crud


class TaskCreateApi(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskApi(generics.ListAPIView):
    # queryset = Task.objects.filter(user=self.request.user)
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
