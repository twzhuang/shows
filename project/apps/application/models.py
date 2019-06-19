from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['no_title'] = "The title field is required"
        elif len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 1:
            errors['no_network'] = "The network field is required"
        elif len(postData['network']) < 2:
            errors['network'] = "Network name should be at least 3 characters"
        if len(postData['description'])<10 and len(postData['description']) > 0:
            errors['description'] = "Description field is optional, but must be at least 10 characters long if provided"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
