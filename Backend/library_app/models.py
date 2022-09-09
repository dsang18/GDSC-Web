from django.db import models

class Books(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    issued = models.BooleanField(default=False)
    issued_by = models.CharField(default='', max_length=5)

    def __str__(self):
        return self.title
    

class Members(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
