from django.http import HttpResponse
from django.shortcuts import render
from newsite.aperson import models

def login(request):
    return render(request, 'template1.html')

def check(request):
    if 'email' in request.GET and request.GET['email']:
	q = request.GET['email']
	try:
	    p = people.objects.filter(email = q)
	except:
	    return render(request, 'template1', {'error': True})
	if (p.password == a):	
	    return render(request, 'template3.html')
	else:
	    return render(request, 'template1.html', {'error': True})
    else:
        return render(request, 'template1', {'error': True})


def register(request):
    return render(request,'template3.html')
'''
'pwd' in request.GET and request.GET['pwd']:
	    a = request.GET['pwd']
	    if (p.password == a):
'''
