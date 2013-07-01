from django.db import models

class people(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    ga = (
	('m','Male'),
	('f','Female'),
    )
    gender =  models.CharField(max_length=1,choices = ga)
    hobbies = models.CharField(max_length=100)
    mclass = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('O', 'others'),
    )
    martial_status = models.CharField(max_length=1,choices = mclass)
