from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.permissions import IsAuthenticated
from models.models import Donor,Location,BloodRequest
from models.serializer import DonorSerializer,BloodRequestSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def index(req):
    user= req.user
    donor = Donor.objects.filter(user=user.id).first()
    if req.method == 'GET':
        if donor == None:
            return Response({"error":"No Donor For User"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response((DonorSerializer(donor)).data)
    elif req.method == 'POST':
        if donor == None: 
            donor= Donor()
        location=Location.objects.filter(id=req.POST['location']).first()
        donor.phone=req.POST['phone']
        donor.address=req.POST['address']
        donor.location=location
        donor.user=user
        donor.blood_group=req.POST['blood_group']
        donor.dob=req.POST['dob']
        donor.last_donated=req.POST['last_donated']
        donor.save()
        return Response((DonorSerializer(donor)).data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def changeStatus(req):
    user= req.user
    donor = Donor.objects.filter(user=user.id).first()
    if donor == None:
        return Response({"error":"No Donor For User"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    donor.status=req.POST['status']
    donor.save()
    return Response({"message":"status changed sucessfully"})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def addBloodRequest(req):
    user= req.user
    location=Location.objects.filter(id=req.POST['location']).first()
    
    request=BloodRequest()
    request.name=req.POST['name']
    request.blood_group=req.POST['blood_group']
    request.amount=req.POST['amount']
    request.date=req.POST['date']
    request.hospital=req.POST['hospital']
    request.location=location
    request.address=req.POST['address']
    request.phone=req.POST['phone']
    request.user=user
    request.save()
    return Response((BloodRequestSerializer(request)).data)
    
    # request.
    