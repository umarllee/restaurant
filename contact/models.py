from django.db import models

class Contact(models.Model):
        name_surname= models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        message= models.TextField(blank= True)

        def __str__(self):
            return self.email

