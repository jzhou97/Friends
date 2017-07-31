from __future__ import unicode_literals

from django.db import models

import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        errors = []

        if len(form_data['name']) == 0:
            errors.append("Name is required.")

        if len(form_data['alias']) == 0:
            errors.append("Alias is required.")

        if len(form_data['email']) == 0:
            errors.append("Email is required.")

        if len(form_data['password']) < 8:
            errors.append("Password should be at least eight characters.")

        if form_data['password'] != form_data['password_confirmation']:
            errors.append("Wrong password.")

        return errors

    def validateLogin(self, form_data):
        errors = []

        #user = User.objects.filter(email = form_data['email']).first()

        if len(form_data['email']) == 0:
            errors.append("Email is required.")

        if len(form_data['password']) == 0:
            errors.append("Password is required.")

        #if user == []:
        #    errors.append("No account available.")

        #if form_data['password']

        return errors

    def createUser(self, form_data):
        password = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(password,bcrypt.gensalt())
        user = User.objects.create(
        name = form_data['name'],
        alias = form_data['alias'],
        email = form_data['email'],
        password = hashed_pw,
        )

        return user

#class FriendManager(models.manager):

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    friends = models.ManyToManyField("self", related_name="friend_by")

    objects = UserManager()

#class Friend(models.Model):
    #    name = models.CharField(max_length=255)
        #alias = models.CharField(max_length=255)
        #email = models.EmailField(max_length=255)
        #password= models.CharField(max_length=255)
        #created_at = models.DateTimeField(auto_now_add=True)
        #updated_at = models.DateTimeField(auto_now=True)

        #objects = FriendManager()
