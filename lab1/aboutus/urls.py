from django.urls import path
from aboutus.views import about_us

urlpatterns = [
    path('', about_us, name="aboutus"),
]
