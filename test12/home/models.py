from django.db import models


class ContactUs(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    address = models.TextField()

    def __str__(self):
        return self.email
    
    