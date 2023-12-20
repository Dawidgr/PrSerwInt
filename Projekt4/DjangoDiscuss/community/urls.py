from django.urls import path
from rest_framework.routers import SimpleRouter

from community import views

app_name = 'community'

urlpatterns = [
    path('all', views.community_list, name='community_list'),
    path('<int:id>', views.community_detail, name='community_detail'),
]
