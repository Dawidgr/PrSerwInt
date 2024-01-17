from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('<int:id>', views.user_detail, name='user_detail'),
    path('<int:id>/follow', views.user_follow, name='user_follow')
]
