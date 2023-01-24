from django.urls import path
from . import views,general,donor,chat
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', views.register),
    path('user/', views.user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    
    path('locations',general.locations),
    
    path('donor',donor.index),
    path('donor/list',donor.getDonors),
    path('donor/changeStatus',donor.changeStatus),
    
    
    path('request/add',donor.addBloodRequest),
    path('request/list',donor.getBloodRequest),
    
    path('chats',chat.list),
    path('chats/add',chat.add),
    path('chats/single',chat.single),
    
]
