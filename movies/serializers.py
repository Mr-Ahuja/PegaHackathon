from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import *
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('vid', 'name', 'disease', 'description')


class VaccinesRegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinesRegistered
        fields = ('username', 'doseNumber', 'vid', 'dose_date', 'provider_name')

class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = ('bid', 'username', 'vid', 'status')

class HealthProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProvider
        fields = ('did', 'providerName', 'totalDose', 'driveDate')