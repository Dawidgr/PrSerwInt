from django.urls import path

from post import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('moderation', views.posts_for_moderation, name='posts_for_moderation'),
    path('moderation/<int:id>', views.post_moderation, name='post_moderation'),
    path('<int:id>/comment', views.comment_add, name='comment_add')
]
