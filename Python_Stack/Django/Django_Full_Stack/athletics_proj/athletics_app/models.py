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

        if len(post_data['gym']) < 2:
            errors['gym'] = 'Please enter at least 2 characters for your gym affiliation.'

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
    gym = models.CharField(max_length=64)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Lift(models.Model):
    snatch = models.IntegerField()
    overhead_squat = models.IntegerField()
    clean = models.IntegerField()
    clean_and_jerk = models.IntegerField()
    back_squat = models.IntegerField()
    front_squat = models.IntegerField()
    deadlift = models.IntegerField()
    push_press = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    lifter = models.ForeignKey(
        User,
        related_name="lifts",
        on_delete=models.CASCADE
    )

class Message(models.Model):
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        related_name="messages",
        on_delete=models.CASCADE
    )

class Comment(models.Model):
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )

    message = models.ForeignKey(
        Message,
        related_name="comments",
        on_delete=models.CASCADE
    )


# Create your models here.
