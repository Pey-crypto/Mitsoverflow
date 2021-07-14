

from django.urls import path
from . import views
appname = "userprofile"

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.userregistration,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    
]
