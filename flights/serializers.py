from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model # If used custom user model

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

class UserSerializer(serializers.ModelSerializer):

	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		# Tuple of serialized model fields (see link [2])
		fields = ("username", "password", "last_name", "first_name")
	def create(self, validated_data):
		username = validated_data.get('username')
		password = validated_data.get('password')
		first_name = validated_data.get('first_name')
		last_name = validated_data.get('last_name')
		user = User(username=username, first_name=first_name, last_name=last_name)
		user.set_password(password)
		user.save()

		return validated_data
