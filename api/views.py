from rest_framework.response import Response
from rest_framework import status
import json;
from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from models.models import Donor

@api_view(['GET', 'POST'])
def register(req):
    data=json.loads(req.body)
    # request
    username = data['username']
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    if User.objects.filter(username=username):
        return Response({"error":"Username already exist! Please try some other username"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if User.objects.filter(email=email).exists():
        return Response({"error":"Email already exist! Please try some other email"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if len(username) > 20:
        return Response({"error":"Username must be under 20 characters"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if password != confirm_password:
        return Response({"error":"Password didn't match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if not username.isalnum():
        return Response({"error":"Username must contain letters"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    CustomUser = get_user_model()
    user = CustomUser(username=username, email=email,first_name=fname,last_name=lname)
    user.set_password(password)
    user.save()
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user(req):
    user= req.user
    donor = Donor.objects.filter(user=user.id).first()
    
    return Response({"fname": user.first_name,
                     'lname':user.last_name,
                     "id":user.id,
                     "username":user.username,
                     "has_donor":donor!= None
                    })


