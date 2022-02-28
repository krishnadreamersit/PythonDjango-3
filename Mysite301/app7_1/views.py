from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
    # User Management
    #1. Creating new user
    # first_name
    # last_name
    # email
    # username
    # password

    # user1 = User.objects.create_user(username='admin2', password='admin2', email='admin2@gmail.com', first_name='Bikki', last_name='Sharma')
    # user1.save()

    # user2 = User.objects.create_user(username='admin3', password='admin3')
    # user2.first_name='Sanjaya'
    # user2.last_name = 'Sharma'
    # user2.save()


    #2. Retrieve all users
    users = User.objects.all()
    for user in users:
        print(user.username, user.password, user.email, user.first_name, user.last_name)

    # Update Password
    user3 = User.objects.get(username='admin3')
    user3.set_password('admin')
    user3.save()
    # user3.delete()

    # Login
    user = authenticate(username='admin', password='admin')
    if user is not None:
        print("Welcome ", user.username)
    else:
        print("Invalid user name or password")
    return HttpResponse("Hello");

# Task
# Create an application which manage users. (CRUD App)
    # List all users
    # Filter users
    # Create new user
    # Edit/Update user
    # Delete user