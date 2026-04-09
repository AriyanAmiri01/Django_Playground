from django.shortcuts import render
from django.http import HttpResponse
from myStartApp.models import Client

# temporary thing just to handle old tables
from datetime import datetime  # import datetime class
from django.utils import timezone  # if you need timezone-aware datetime

# Per login 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



# I view per fare il login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


dt = datetime(2026, 3, 31, 12, 0)


def getIndex(request):
    if request.user.is_authenticated:
        #showing the home page for a special client
        return render(request, "index_authenticated.html")
    else:
        # Returns the index page
        return render(request, "Index.html")


# messages.success, info, warning, error

def getLogin(request):
    # Checking the request type
    if request.method == "POST":
        # Checking the form type 
        form_type = request.POST.get("form_type")
        
        if form_type == "login":
        # Login request
            #Getting datas
            email1 = request.POST.get("email", "").strip()  #just skipping white spaces
            password1 = request.POST.get("password", "").strip() # just skipping white spaces
            try:
                username1 = User.objects.get(email=email1).username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect("login")
           
           
            messages.info(request, "we are tying to login you")
            user = authenticate(request, username=username1, password=password1)
            if user:
                login(request, user)
                return redirect("index_authenticated")
            else:
                messages.error(request, "Invalid username or password")        
                return redirect("login")


        elif form_type =="signup":
        # Sign up request
            first_name = request.POST.get("first-name")
            last_name = request.POST.get("last-name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            password2 = request.POST.get("reapet-password")
            # Basic validation
            if password1 != password2:
                messages.error(request, "Passwords do not match")
                return redirect("login")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect("login")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
                return redirect("login")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                login(request, user)
                return redirect("Index.html")


        else:
        # Unknown POST request
            return redirect("Index.html")

    else:
        print("hello3")
        return render(request, "Login.html")


def getIndexAuthenticated(request):
    return render(request, "index_authenticated.html")

def getDocs(request):
    # Returns the documents page
    return render(request, "Docs.html")

def getAboutMe(request):
    # Returns the AboutMe page
    return render(request, "AboutMe.html")

def client_request(request):
    # Create default clients if they don't exist
    if not Client.objects.exists():
        Client.objects.create(first_name="Magnus", last_name="Carlsen", email="magnusCarlsen@gmail.com", password="ABC123")
        Client.objects.create(first_name="Hikaru", last_name="Nakamura", email="HikaruNakamura@gmail.com", password="ABC123")
    
    # Query all clients
    clients = Client.objects.all()
    
    # Display clients in the browser
    response_text = ", ".join([f"{c.first_name} {c.last_name}" for c in clients])
    return HttpResponse(f"Clients in DB: {response_text}")

