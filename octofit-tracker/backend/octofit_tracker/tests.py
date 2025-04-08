from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctofitTrackerTests(APITestCase):

    def test_create_user(self):
        data = {'email': 'testuser@example.com', 'name': 'Test User', 'age': 25}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_team(self):
        data = {'name': 'Team A', 'members': ['user1', 'user2']}
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_activity(self):
        data = {'user': 'user1', 'type': 'running', 'duration': 30, 'date': '2025-04-08'}
        response = self.client.post('/api/activity/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_leaderboard_entry(self):
        data = {'team': 'Team A', 'points': 100}
        response = self.client.post('/api/leaderboard/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_workout(self):
        data = {'name': 'Morning Run', 'description': 'A quick morning run', 'duration': 20}
        response = self.client.post('/api/workouts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
