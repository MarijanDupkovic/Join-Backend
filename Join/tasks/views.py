from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CategoryItem, ContactItem, TaskItem
from .serializers import CategoryItemSerializer, ContactItemSerializer, LoginSerializer, RegistrationSerializer, TaskItemSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class LoginView(APIView):
    
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            userData = serializer.validated_data
            user = get_user_model().objects.get(email=userData['email'])
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
   
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
  
class CategoryItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoryItemSerializer
    queryset = CategoryItem.objects.all()

class TaskItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskItemSerializer
    queryset = TaskItem.objects.all()
    def taskhandler(self, request, format=None):
         if request.method == 'GET':
            tasks = TaskItem.objects.all()
            serializer = TaskItemSerializer(tasks, many=True)
            return Response(serializer.data)
         if request.method == 'POST':
            serializer = TaskItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
                
class ContactItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactItemSerializer
    queryset = ContactItem.objects.all()
    def contacthandler(self, request, format=None):
        if request.method == 'GET':
            contacts = ContactItem.objects.all()
            serializer = ContactItemSerializer(contacts, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = ContactItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         
