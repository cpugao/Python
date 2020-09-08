from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        print(post_data)

        if len(post_data['title']) < 2:
            errors['title'] = "Please enter a title of at least 2 characters!"

        if len(post_data['network']) < 3:
            errors['network'] = "Please enter a network of at least 3 characters!"

        if not post_data['release_date'].isnumeric():
            errors['release_date'] = "Numerical values only for the date!"

        if len(post_data['desc']) < 10:
            errors['desc'] = "Please enter a description of at least 10 characters!"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=64)
    network = models.CharField(max_length=64)
    release_date = models.DateField()
    desc = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()



# Create your models here.
