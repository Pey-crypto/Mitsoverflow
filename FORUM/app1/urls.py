from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('landing_page/', views.landing, name='landing_page'),
]