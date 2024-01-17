from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('<int:id>', views.notification_detail, name='notification_detail')
]
