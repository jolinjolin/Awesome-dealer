from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarMake, CarModel, CarDealer
from .restapis import get_dealers_from_cf, get_request, get_dealer_by_id_from_cf, get_dealer_reviews_from_cf, post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/about.html', context)

# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    print("Log out the user '{}'".format(request.user.username))
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            user.is_superuser = True
            user.is_staff=True
            user.save() 
            login(request, user)
            
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/user_registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


def get_dealerships(request):
    if request.method == "GET":
        url = "https://d45509ab.us-south.apigw.appdomain.cloud/api/dealership"
        dealerships = get_dealers_from_cf(url)
        context = {}
        context["dealers"] = dealerships
        return render(request, 'djangoapp/index.html', context)

def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = "https://d45509ab.us-south.apigw.appdomain.cloud/api/dealership"
        dealer = get_dealer_by_id_from_cf(dealer_url, id=id)
        context["dealer"] = dealer
    
        review_url = "https://d45509ab.us-south.apigw.appdomain.cloud/api/review"
        reviews = get_dealer_reviews_from_cf(review_url, id=id)
        context["reviews"] = reviews
        
        return render(request, 'djangoapp/dealer_details.html', context)

def add_review(request, id):
    if request.method == "GET" :
            context={}
            dealer_url = "https://d45509ab.us-south.apigw.appdomain.cloud/api/dealership"
            dealer = get_dealer_by_id_from_cf(dealer_url, id)
            context['dealership'] = dealer
            cars = CarModel.objects.all()  
            print(cars)         
            context['cars'] = cars
            return render(request, 'djangoapp/add_review.html', context)
    if request.method == 'POST':
        if request.user.is_authenticated:
            review_url = "https://d45509ab.us-south.apigw.appdomain.cloud/api/review"
            username = request.user.username
            car_id = request.POST["car"]
            car = CarModel.objects.get(pk=car_id)
            review = {}
            review["time"] = datetime.utcnow().isoformat()
            review["dealership"] = id
            review["review"] = request.POST['review']
            review["name"] = username
            review["purchase"] = False
            if "purchased" in request.POST:
                if request.POST["purchased"] == 'on':
                    payload["purchase"] = True
            review["purchase_date"] = request.POST['purchase_date']
            review["car_make"] = car.make.name
            review["car_model"] = car.name
            review["car_year"] =  int(car.year.strftime("%Y"))

            d = {}
            d["review"] = review
            # payload = json.dumps(d, indent = 4)
            post_request(review_url, d, id=id)

        return redirect("djangoapp:dealer_details", id=id)
