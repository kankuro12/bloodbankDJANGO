
from django.urls import path,include
from .views import data
urlpatterns = [
    path('api/', include('api.urls')),
    path('dashboard/', include('dashboard.urls')),
]
