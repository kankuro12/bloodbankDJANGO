from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def register(req):
    # request
    username = req.POST['username']
    fname = req.POST['fname']
    lname = req.POST['lname']
    email = req.POST['email']
    password = req.POST['password']
    confirm_password = req.POST['confirm_password']

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
def load(request):
    return Response({"Asdfsda": "ASdfasdf"})
