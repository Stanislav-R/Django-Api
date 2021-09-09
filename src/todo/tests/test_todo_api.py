import json

from django.test import TestCase
from rest_framework import status

from rest_framework.test import APIRequestFactory, APIClient

from ..models import Todo

from ..views import TodoViewSet


class ApiPageTest(TestCase):
    def test_todo_loads_properly(self):
        """The todo api page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/api/todo/')
        self.assertEqual(response.status_code, 200)


class ViewSetTest(TestCase):

    def test_view_set(self):
        """The TodoViewSet works properly"""
        request = APIRequestFactory().get("")
        todo_list = TodoViewSet.as_view({'get': 'retrieve'})
        task = Todo.objects.create(title="Task_Test")
        response = todo_list(request, pk=task.pk)
        self.assertEqual(response.status_code, 200)

    def test_todo_create(self):
        data = json.dumps({
            "title": "Task 1",
            "description": "Test Task 1"
        })
        client = APIClient()
        response = client.post('/api/todo/todo_list/', data=data, content_type='application/json')
        # Check if you get a 201 back:
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check to see if Todo was created
        self.assertEqual(response.data['title'], 'Task 1')
