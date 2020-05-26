from django.db import models

class Res(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    mailid = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)

class Meta:
    db_table = 'stud1'
