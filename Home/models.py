from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=50)
    message = models.TextField()
    created_on = models.DateField()

    def __str__(self):
        return self.first_name