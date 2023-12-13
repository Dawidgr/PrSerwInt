from django.urls import path
from rest_framework.routers import SimpleRouter

from post import views

app_name = 'post'

urlpatterns = [
    path('all', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
]
