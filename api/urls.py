from django.urls import path
from . import views,general,donor
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', views.register),
    path('load/', views.load),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('locations',general.locations),
    
    path('donor',donor.index),
    path('donor/list',donor.getDonors),
    path('donor/changeStatus',donor.changeStatus),
    
    
    path('request/add',donor.addBloodRequest),
    path('request/list',donor.getBloodRequest),
    
    
    
]
