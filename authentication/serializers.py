from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=35, min_length=2, required=True)
    last_name = serializers.CharField(max_length=35, min_length=2, required=True)
    password1 = serializers.CharField(max_length=64, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=64, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=200, required=True)
    username = serializers.CharField(max_length=255, min_length=2, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password1 = attrs.get('password1', '')
        password2 = attrs.get('password2', '')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already taken')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This user is already taken')

        if password1 != password2:
            raise serializers.ValidationError('Passwords are not same')    
        
        return attrs 
        
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password1'], 
            )
        return user


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=255)
    password = serializers.CharField(min_length=4, max_length=64)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('No user found')
        data['user'] = user
        return data
