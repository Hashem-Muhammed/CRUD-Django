from django.urls import path
from contactus.views import contact_us

urlpatterns = [
    path('', contact_us, name="contactus"),
]
