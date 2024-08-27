from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class RegistrationSerializator(serializers.ModelSerializer):
    balance = serializers.DecimalField(source = 'balance.balance', max_digits = 10, decimal_places = 2, read_only = True)
    password = serializers.CharField(write_only = True)
    slug = serializers.SlugField(required = False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password = make_password(password)
        return get_user_model().objects.create(password = password, **validated_data)
        
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'slug', 'password', 'last_name', 'email', 'balance']


class ProfileSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(source = 'balance.balance', max_digits = 10, decimal_places = 2, read_only = True)
    date_joined = serializers.DateTimeField(read_only = True)

    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'slug', 'date_joined', 'balance')