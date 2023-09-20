from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework.exceptions import ValidationError
from django.db import models
    
User = get_user_model()

# login 
class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'role',
        )
        read_only_fields = (settings.LOGIN_FIELD,)



# registration
class CustomUserCreateSerializer(UserCreateSerializer):

    middle_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)

    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            "role",            
            "first_name",
            "middle_name",
            "last_name",
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
        )

    # added

    
    def clean_user_data(self, validated_data):
        return {
            'email' : validated_data.get('email', ''),
            'password' : validated_data.get('password', ''),        
            'username' : validated_data.get('username', ''),
            'first_name' : validated_data.get('first_name', ''),
            'middle_name' : validated_data.get('middle_name', ''), 
            'last_name' : validated_data.get('last_name', ''),
            'role': validated_data.get('role', ''),
        }


    def validate(self, attrs):
        user_data = self.clean_user_data(attrs)
        user = User(**user_data)
        password = user_data.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        role = validated_data.get("role")  # Use validated_data here
        if role == "ADMIN":
            user.is_staff = True
            user.is_superuser = True
            user.save(update_fields=["is_staff", "is_superuser"])

        return user



    def perform_create(self, validated_data):
        with transaction.atomic():

            user_data=self.clean_user_data(validated_data)
            user = User.objects.create_user(**user_data)
            if settings.SEND_CONFIRMATION_EMAIL:
                user.is_active = True
                user.save(update_fields=["is_active"])

        return user
    