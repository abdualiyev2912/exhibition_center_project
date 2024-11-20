from django.db import models
from exhibitions.validators import validate_file_extension, validate_file_size


class Exhibition(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=60)
    image = models.ImageField(upload_to='exhibition_images/', validators=[validate_file_size, validate_file_extension])


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    theme = models.CharField(max_length=150)
    description = models.TextField()