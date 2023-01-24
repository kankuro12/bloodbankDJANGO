from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.TextField()

class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    last_donated = models.DateField(null=True)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,null=True)
    blood_group = models.CharField(max_length=3,null=True)
    status=models.BooleanField(default=True)
  
    

    

class BloodRequest(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3)
    phone = models.CharField(max_length=13,null=True)
    amount = models.IntegerField()
    date = models.DateField()
    hospital = models.CharField(max_length=50)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    completed=models.BooleanField(default=False)

class Chat(models.Model):
    id=models.AutoField(primary_key=True)
    ident=models.CharField(max_length=50)
    senderName=models.CharField(max_length=50)
    receiverName=models.CharField(max_length=50)
    from_id=models.IntegerField(null=True)
    to_id=models.IntegerField(null=True)
    message=models.TextField()
    
    

