from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def blogdetails(request):
    return render(request,'blog-details.html')

def portfoliodetails(request):
    return render(request,'portfolio-details.html')

def service(request):
    return render(request,'service-detals.html')

def starter(request):
    return render(request,'starter-page.html')
