from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import FormSignUp

def signup(request):
    if request.method == "POST":
        form = FormSignUp(request.POST)
        
        if form.is_valid():
            login(request, user=form.save())
            
            return redirect("front_page")
        
    else:
        form = FormSignUp()
        
    context = {
        "form" : form
    }
    
    return render(request, "core/signup.html", context)

# Create your views here.
def front_page(request):
    return render(request, "core/front_page.html")


