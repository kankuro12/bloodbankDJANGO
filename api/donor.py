from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.permissions import IsAuthenticated
from models.models import Donor,Location,BloodRequest
from models.serializer import DonorSerializer,BloodRequestSerializer,BloodRequestListSerializer
from datetime import datetime,timedelta
import json;
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
            
        data=json.loads(req.body)
        location=Location.objects.filter(id=data['location']).first()
        donor.phone=data['phone']
        donor.address=data['address']
        donor.location=location
        donor.user=user
        donor.blood_group=data['blood_group']
        donor.dob=data['dob']
        donor.last_donated=data['last_donated']
        donor.save()
        return Response((DonorSerializer(donor)).data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def changeStatus(req):
    user= req.user
    donor = Donor.objects.filter(user=user.id).first()
    if donor == None:
        return Response({"error":"No Donor For User"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    data=json.loads(req.body)
    donor.status=data['status']
    donor.save()
    return Response({"message":"status changed sucessfully"})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def addBloodRequest(req):
    user= req.user
    data=json.loads(req.body)
    location=Location.objects.filter(id=data['location']).first()
    request=BloodRequest()
    request.name=data['name']
    request.blood_group=data['blood_group']
    request.amount=data['amount']
    request.date=data['date']
    request.hospital=data['hospital']
    request.location=location
    request.address=data['address']
    request.phone=data['phone']
    request.user=user
    request.save()
    return Response((BloodRequestSerializer(request)).data)
    
    # request.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getDonors(req):
    data=json.loads(req.body)
    location=Location.objects.filter(id=data['location']).first()
    blood_group=data['blood_request']
    date = datetime.now()
    ninety_days_ago =( date - timedelta(days=90)).date()
    donors=Donor.objects.filter(location=location,blood_group=blood_group,last_donated__lte=ninety_days_ago)
    alldatas=[]
    for donor in donors:
        alldatas.append((DonorSerializer(donor)).data)
    return Response(alldatas)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getBloodRequest(req):
    type=req.GET['type']  
    data=json.loads(req.body)
    
    if type=="1":
        location=Location.objects.filter(id=data['location']).first()
        blood_group=data['blood_request']
        date = datetime.now().date()
        requests=BloodRequest.objects.filter(location=location,date__gte=date,blood_group=blood_group).order_by('date')
    if type=="2":
        
        date = datetime.now().date()
        requests=BloodRequest.objects.filter(date=date)       

    alldatas=[]
    for request in requests:
        alldatas.append((BloodRequestSerializer(request)).data)
    return Response(alldatas)
    
    
    
    
