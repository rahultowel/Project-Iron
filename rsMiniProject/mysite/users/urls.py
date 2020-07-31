from django.urls import path
from . import views

app_name='users'
urlpatterns =[
path('<str:user_id>/', views.ProfileView.as_view(), name='profile'),
path('<str:user_id>/mypolls/', views.MyPolls.as_view(), name='mypolls'),
path('<str:user_id>/notification/', views.Notification.as_view(), name='notification'),
]
