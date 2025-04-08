from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor Odinson', age=30, team='Blue Team'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', age=35, team='Gold Team'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot Alderson', age=28, team='Blue Team'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Dade Murphy', age=25, team='Gold Team'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', age=22, team='Blue Team'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team', members=[user.email for user in users if user.team == 'Blue Team']),
            Team(_id=ObjectId(), name='Gold Team', members=[user.email for user in users if user.team == 'Gold Team']),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0].email, type='Cycling', duration=60, date='2025-04-01'),
            Activity(_id=ObjectId(), user=users[1].email, type='Crossfit', duration=120, date='2025-04-02'),
            Activity(_id=ObjectId(), user=users[2].email, type='Running', duration=90, date='2025-04-03'),
            Activity(_id=ObjectId(), user=users[3].email, type='Strength', duration=30, date='2025-04-04'),
            Activity(_id=ObjectId(), user=users[4].email, type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team='Blue Team', points=300),
            Leaderboard(_id=ObjectId(), team='Gold Team', points=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
