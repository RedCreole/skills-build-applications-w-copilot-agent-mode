from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Zero Cool', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Crash Override', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(name='Blue Team', members=[user.id for user in users[:3]])
        team.save()
        team = Team(name='Gold Team', members=[user.id for user in users[3:]])
        team.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date='2025-04-01'),
            Activity(user=users[1], type='Crossfit', duration=120, date='2025-04-02'),
            Activity(user=users[2], type='Running', duration=90, date='2025-04-03'),
            Activity(user=users[3], type='Strength', duration=30, date='2025-04-04'),
            Activity(user=users[4], type='Swimming', duration=75, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team, score=100) for team in Team.objects.all()
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))