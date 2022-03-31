from django.urls import path, include
from profiles.views import CreateProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', CreateProfileView.as_view(), name='register')
]