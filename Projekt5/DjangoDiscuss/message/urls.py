from django.urls import path
from message import views

app_name = 'message'

urlpatterns = [
    path('<int:id>', views.message_detail, name='message_detail'),
    path('add', views.message_add, name='message_add')
]
