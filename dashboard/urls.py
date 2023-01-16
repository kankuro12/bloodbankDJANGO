from django.urls import path
from . import views,location,donor
urlpatterns = [
    path('', views.index,name="dashboard"),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    
    #XXX locations
    path('locations/', location.index,name="locations"),
    path('locations/add/', location.add,name="locations.add"),
    path('locations/edit/', location.edit,name="locations.edit"),
    # path('locations/del/', location.delete,name="locations:del"),
    
    #XXX Donors
    path('donors/', donor.index,name="donors"),
    path('requests/', donor.bloodRequests,name="bloodrequests"),
    
    
]