from rest_framework import serializers
from .models import ContactItem, TaskItem, CategoryItem
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

MIN_LENGTH = 8

class ContactItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactItem
        fields = ('id','first_name', 'last_name', 'email', 'phone')
        
class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = '__all__'

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ('title', 'description', 'prio', 'due_date', 'category', 'assigned_users','author')
        extra_kwargs = {
            "prio": {"required": False},
            "assigned_users": {"required": False},
    }
                
           
class RegistrationSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True,
    min_length=MIN_LENGTH,
    error_messages={
      "min_length": f"Password must be longer than {MIN_LENGTH} characters."
    },
    style={'input_type': 'password', 'placeholder': 'Password'}
  )
  password2 = serializers.CharField(
    write_only=True,
    min_length=MIN_LENGTH,
    error_messages={
      "min_length": f"Password must be longer than {MIN_LENGTH} characters."
    },
    style={'input_type': 'password', 'placeholder': 'Password'}
  )
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'password2')
    extra_kwargs = {
      "username": {"write_only": True, "required": True},
      "email": {"write_only": True, "required": True},
      "password": {"write_only": True , "required": True},
      "password2": {"write_only": True , "required": True},
    }

  def validate(self, data):
    if data["password"] != data["password2"]:
      raise serializers.ValidationError("Password does not match.")
    return data
  
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data["username"],
      email=validated_data["email"],
    )

    user.set_password(validated_data["password"])
    user.save()

    return user

def authenticate_with_email_and_password(email, password):
    user = get_user_model()
    try:
        user = user.objects.get(email=email)
        if user.check_password(password):
            return user
    except user.DoesNotExist:
        return None

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password', 'placeholder': 'Password'})
    
    class Meta:
        model = User
        fields = ('email','password')
        read_only_fields = ('username', )

    def validate(self, data):
        user = authenticate_with_email_and_password(data["email"], data["password"])
        if user:
            if user.is_active:
                return {'username': user.username, 'email': user.email, 'password': user.password}
        raise serializers.ValidationError("Incorrect Credentials")

