from rest_framework import serializers
from .models import Donor,BloodRequest
from django.contrib.auth.models import User

#Donor Serializer
class DonorSerializer(serializers.ModelSerializer):
    location_name=serializers.CharField(source='location.name')
    user_id=serializers.CharField(source='user.id')
    
    class Meta:
        model = Donor
        fields = ('id', 'phone', 'dob', 'address', 'location', 'blood_group','location_name','user_id')
#request Serializer
class BloodRequestSerializer(serializers.ModelSerializer):
    location_name=serializers.CharField(source='location.name')
    fname=serializers.CharField(source='user.first_name')
    lname=serializers.CharField(source='user.last_name')
    user_id=serializers.CharField(source='user.id')
    class Meta:
        model = BloodRequest
        fields = ('id', 'name','phone','user_id', 'hospital', 'address', 'blood_group','location_name','amount','fname','lname')
class BloodRequestListSerializer(serializers.ListSerializer):
    child = BloodRequestSerializer()
    allow_null = True
    many = True
      
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
