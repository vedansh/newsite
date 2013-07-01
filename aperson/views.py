from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from aperson import models

def login(request):
    return render(request, 'template1.html', {'error': False})

def errlogin(request):
    return render(request, 'template1.html', {'error': True})

def check(request):
    if request.method == 'POST':
    	if request.POST.get('email'):
    	    q = request.POST.get('email')
	    if(models.people.objects.filter(email = q)):
	        p = models.people.objects.get(email = q)
	    else:
	    	return  HttpResponseRedirect('/errlogin/')
	    if request.POST.get('pwd'):
	    	a = request.POST.get('pwd')
	        if (p.password == a):	
	            return render(request, 'template3.html')
    return  HttpResponseRedirect('/errlogin/')

def search(request):
    p = models.people.objects.all()
    if request.method == 'POST':
        if  request.POST.get('fname'):
            p=p.filter(first_name = request.POST.get('fname').lower())
        if  request.POST.get('lname'):
            p=p.filter(last_name = request.POST.get('lname').lower())
        if request.POST.get('email'):
	    p=p.filter(email = request.POST.get('email'))
	if request.POST.get('company'):
	    p=p.filter(company = request.POST.get('company'))
	if request.POST.get('age'):
	    try:
	        p=p.filter(age = request.POST.get('age'))
	    except:
		p = []
	if request.POST.get('gender'):
	    p=p.filter(gender = request.POST.get('gender'))
	if request.POST.get('mstatus'):
	    p=p.filter(martial_status = request.POST.get('mstatus'))
    return render(request,'template4.html',{'data':p})

def newsearch(request):
    return render (request,'template3.html')


def register(request):
    return render(request,'template2.html')

def check2(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('fname'):
            errors.append('Enter a first name.')
	else:
	    fn = request.POST.get('fname')
	    fn = fn.lower()
        if not request.POST.get('lname'):
            errors.append('Enter a last name.')
	else:
	    ln = request.POST.get('lname')
	    ln = ln.lower()
        if request.POST.get('email') and '@' in request.POST['email']:
	    eml = request.POST.get('email')
	    if  models.people.objects.filter(email = eml):
	        errors.append('This email is already in use')
	else:
            errors.append('Enter a valid e-mail address.')
	if  request.POST.get('pwd'):
	    pwd = request.POST.get('pwd')
	    if  request.POST.get('cpwd'):
		cpwd = request.POST.get('cpwd')
		if(cpwd != pwd):
            	    errors.append(' Both passsword must be same.')
	    else:
 	        errors.append(' Password field can not be left empty.')
	else:
 	    errors.append(' Password field can not be left empty.')
	if not request.POST.get('company'):
            errors.append('please enter a company.')
	else:
	    cmpny = request.POST.get('company')
	if not request.POST.get('age'):
            errors.append('Please specify your age.')
	else:
	    ag = request.POST.get('age')
	if not request.POST.get('gender'):
            errors.append('Specify your gender.')
	else:
	    gn = request.POST.get('gender')
	if not request.POST.get('hobbies'):
            errors.append(' Please tell your hobbies.')
	else:
	    hb = request.POST.get('hobbies')
	if not request.POST.get('mstatus'):
            errors.append('Specify your martial staus.')
	else:
	    mstatus = request.POST.get('mstatus')
        if not errors:
	    try:
                p = models.people( first_name = fn,
        	    last_name = ln,
	            company = cmpny ,
        	    email = eml ,
	            password = pwd ,
	            age = ag ,
	            gender =  gn ,
	            hobbies = hb ,
	            martial_status = mstatus )
	    except:
		errors.append('Specify a valid age between 10 and 100 in numeral format.')
	    else:
	    	p.save()
            return render (request,'template3.html')
    return render(request, 'template2.html',
        {'errors': errors})



