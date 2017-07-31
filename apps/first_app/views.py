from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, UserManager
import bcrypt
#CONTROLLER
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def currentUser(request):
    id = request.session['user_id']
    return User.objects.get(id=id)

def success(request):
    if 'user_id' in request.session:
        current_user = currentUser(request)

        friends = current_user.friends.all()

        users = User.objects.exclude(id__in=friends).exclude(id=current_user.id)

        context = {
            'users': users,
            'friends': friends,
            'current_user': current_user

        }
        return render(request, 'first_app/success.html', context)

    return redirect('/')

def register(request):
    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/success')

        flashErrors(request, errors)

    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.validateLogin(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email']).first()

            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)
                hashed_pw = bcrypt.hashpw(password, user_password)
                if hashed_pw == user.password:
                    request.session['user_id'] = user.id
                    return redirect('/success')

            errors.append("Invalid account information.")

        flashErrors(request, errors)

    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')

    return redirect('/')

def flashErrors(request, errors):
    for errors in errors:
        messages.error(request, errors)

def addFriend(request, id):
    if request.method == "POST":
        if 'user_id' in request.session:
            current_user = currentUser(request)
            friend = User.objects.get(id=id)
            current_user.friends.add(friend)
            return redirect(reverse('success'))
    return redirect('/')

def removeFriend(request, id):
    if request.method == "POST":
        if 'user_id' in request.session:
            current_user = currentUser(request)
            friend = User.objects.get(id=id)
            current_user.friends.remove(friend)
            return redirect(reverse('success'))
    return redirect('/')

def viewProfile(request, id):
    current_user = currentUser(request)

    friends = current_user.friends.all()

    users = User.objects.exclude(id__in=friends).exclude(id=current_user.id)

    context = {
        'users': users,
        'friends': friends,
        'current_user': current_user
    }

    if request.method == "POST":
        if 'user_id' in request.session:
            current_user = currentUser(request)
            user = User.objects.get(id=id)
            return render(request, 'first_app/profile.html', context)
    return redirect('/')

def viewfriendProfile(request, id):
    current_user = currentUser(request)

    friends = current_user.friends.all()

    users = User.objects.exclude(id__in=friends).exclude(id=current_user.id)

    context = {
        'users': users,
        'friends': friends,
        'current_user': current_user
    }

    if request.method == "POST":
        if 'user_id' in request.session:
            current_user = currentUser(request)
            friend = User.objects.get(id=id)
            return render(request, 'first_app/friend.html', context)
    return redirect('/')
