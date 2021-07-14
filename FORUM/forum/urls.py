
from . import views
from django.urls import path
from django.urls import re_path
from django.conf.urls import url
app_name = "forum"

base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'

urlpatterns = [

   path('',views.home,name="home"), 
   path('new_forum/',views.new_forum,name="new_forum"), 
   path('new_thread/',views.new_thread,name="new_thread"), 
   path('profile/',views.profile,name="profile"), 
   path('open_thread/<str:t_id>/', views.open_thread, name='open_thread'),
   path('delete_thread/<str:t_id>/', views.delete_thread, name='delete_thread'),
   path('delete_reply/<str:r_id>/', views.delete_reply, name='delete_reply'),
   path('open_forum/<str:f_id>/', views.open_forum, name='open_forum'),
   path('join_forum/', views.join_forum, name='join_forum'),
   path('exit_forum/', views.exit_forum, name='exit_forum'),
   path('reply/',views.reply,name="reply"), 
   re_path(r'^(?P<base64string>{})'.format(base64_pattern),views.forum_view,name="forum_view"),
]
