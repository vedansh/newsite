from django import forms

class peopleform(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=20)
    company = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    age = forms.IntegerField()
    ga = (
	('M','Male'),
	('F','Female'),
    )
    gender =  forms.CharField(max_length=1,choices = ga)
    hobbies = forms.CharField(max_length=100)
    mclass = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('O', 'others'),
    )
    martial_status = forms.CharField(max_length=1,choices = mclass)
