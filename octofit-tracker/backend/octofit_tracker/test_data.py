# Test data for populating the octofit_db database

test_users = [
    {"username": "student1", "email": "student1@example.com", "password": "password123"},
    {"username": "student2", "email": "student2@example.com", "password": "password123"},
    {"username": "student3", "email": "student3@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team A", "members": ["student1", "student2"]},
    {"name": "Team B", "members": ["student3"]},
]

test_activities = [
    {"user": "student1", "type": "running", "duration": 30, "distance": 5},
    {"user": "student2", "type": "walking", "duration": 60, "distance": 4},
    {"user": "student3", "type": "cycling", "duration": 45, "distance": 15},
]

test_leaderboard = [
    {"user": "student1", "points": 100},
    {"user": "student2", "points": 80},
    {"user": "student3", "points": 120},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day", "duration": 30},
    {"name": "Evening Walk", "description": "A relaxing walk in the park", "duration": 60},
    {"name": "Cycling Challenge", "description": "A 15km cycling route", "duration": 45},
]
