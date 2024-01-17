from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('notification', views.notification_list, name='notification_list'),
    path('notification/<int:id>', views.notification_detail, name='notification_detail')
]
