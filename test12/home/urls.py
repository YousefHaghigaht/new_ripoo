from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('contactus/',views.ContactUsView.as_view(),name='contact_us'),
]