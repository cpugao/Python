from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'Please enter at least 2 characters for your first name.'

        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Please enter at least 2 characters for your last name.'

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Please enter a valid email address.'

        if len(post_data['password']) < 6:
            errors['password'] = 'Please enter at least 6 characters for your password.'

        if post_data['password'] != post_data['password_confirm']:
            errors['password_confirm'] = 'Please ensure your password matches the confirmation.'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #overriding the objects class variable
    objects = UserManager()

# Create your models here.
