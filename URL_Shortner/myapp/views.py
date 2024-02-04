from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import LongToShort
# Create your views here.
def hello_world(request):
	return HttpResponse("Hello World")

def home_page(request):
    context = {
        "submitted": False,
        "error": False
    }
    if request.method == 'POST':
        
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']

        try:
            obj = LongToShort(Long_url=long_url, short_url=custom_name)
            obj.save()

            date = obj.date
            clicks = obj.clicks
            context["long_url"] = long_url
            context["short_url"] = request.build_absolute_uri() + custom_name
            context["date"] = date
            context["clicks"] = clicks
            context["submitted"] = True

        except:
        	context["error"] = True
    else:
        print("There is no data")

    return render(request, "index.html", context)


def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url=short_url)
    
    if len(row) == 0:
        return HttpResponse("No such short URL exists")

    obj = row[0]
    long_url = obj.Long_url

    obj.clicks = obj.clicks + 1
    obj.save()

    return redirect(long_url)

def task(request):
	context={
	"my_name":"Adarsh",
	"x":13
	}
	return render(request,"test.html",context)

def analytics(request):
	return render(request,'analytics.html')

def all_analytics(request):

	rows = LongToShort.objects.all()

	context = {
	"rows":rows
	}
	return render(request,"all-analytics.html",context)

def loginFunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have successfully logged in')
            return render(request,"index.html")
        else:
            return render(request,"login.html")
    return render(request, "login.html")

def registerFunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            # Handle the case where the username is not unique
            # You might want to display an error message or redirect to a registration form
            return render(request, 'register.html', {'error_message': 'Username already exists. Please choose a different one.'})

        # Create a new user
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect or do any other necessary actions
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')  # You might want to handle the case where authentication fails

    return render(request, 'register.html')


def logoutFunc(request):
    logout(request)
    return render(request,"index.html")