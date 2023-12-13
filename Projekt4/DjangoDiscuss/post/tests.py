from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_all_posts(self):
        response = self.client.get(reverse('post:post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {'title': 'Test Post', 'description': 'Test Description', 'user_added': self.user.id}
        response = self.client.post(reverse('post:post_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_create_post_without_title(self):
        data = {'description': 'Test Description', 'user_added': self.user.id}
        response = self.client.post(reverse('post:post_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_without_description(self):
        data = {'title': 'Test Post', 'user_added': self.user.id}
        response = self.client.post(reverse('post:post_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Post.objects.count(), 0)

    def test_edit_nonexistent_post(self):
        non_existent_post_id = 999
        updated_data = {'title': 'Updated Post', 'description': 'Updated Description', 'user_added': self.user.id}
        response = self.client.put(reverse('post:post_detail', args=[non_existent_post_id]), updated_data,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_post(self):
        non_existent_post_id = 999
        response = self.client.delete(reverse('post:post_detail', args=[non_existent_post_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_post_detail(self):
        post = Post.objects.create(title='Test Post', description='Test Description', user_added=self.user)
        response = self.client.get(reverse('post:post_detail', args=[post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_update_post(self):
        post = Post.objects.create(title='Test Post', description='Test Description', user_added=self.user)
        updated_data = {'title': 'Updated Post', 'description': 'Updated Description', 'user_added': self.user.id}
        response = self.client.put(reverse('post:post_detail', args=[post.id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'Updated Post')

    def test_delete_post(self):
        post = Post.objects.create(title='Test Post', description='Test Description', user_added=self.user)
        response = self.client.delete(reverse('post:post_detail', args=[post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
