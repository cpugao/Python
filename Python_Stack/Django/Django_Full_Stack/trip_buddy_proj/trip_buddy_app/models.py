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

class TripManager(models.Manager):
    def basic_validator(self, post_data):

        errors = {}

        if len(post_data['destination']) < 3:
            errors['destination'] = "Please enter a destination of at least 3 characters!"

        if len(post_data['plan']) < 3:
            errors['plan'] = "Please enter a plan of at least 3 characters!"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Trip(models.Model):
    destination = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tourist = models.ForeignKey(
        User,
        related_name="trips",
        on_delete=models.CASCADE
    )

    objects = TripManager()

# Create your models here.
