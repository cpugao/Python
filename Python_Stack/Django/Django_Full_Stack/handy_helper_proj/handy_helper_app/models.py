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

class JobManager(models.Manager):
    def basic_validator(self, post_data):

        errors = {}

        if len(post_data['title']) < 3:
            errors['first_name'] = 'Please enter at least 2 characters for your title.'

        if len(post_data['desc']) < 3:
            errors['last_name'] = 'Please enter at least 2 characters for your description.'

        if len(post_data['location']) < 3:
            errors['password'] = 'Please enter at least 3 characters for your location.'

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

class Job(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    location = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    helper = models.ForeignKey(
        User,
        related_name="jobs",
        on_delete=models.CASCADE
    )

    objects = JobManager()



# Create your models here.
