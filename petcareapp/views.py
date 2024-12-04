from django.shortcuts import render, redirect
from petcareapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def blogdetails(request):
    return render(request,'blog-details.html')

def portfoliodetails(request):
    return render(request,'portfolio-details.html')

def servicedetails(request):
    return render(request,'service-detals.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == 'POST':
        mycontact=Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')


def pricing(request):
    return render(request,'pricing.html')
