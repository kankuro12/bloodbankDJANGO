from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from models.models import Location

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def locations(request):
    locations = Location.objects.all().values()
    return Response(locations)

def addRequest(req):
    return Response({"name":"name"})