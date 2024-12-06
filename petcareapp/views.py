from django.shortcuts import render, redirect

from petcareapp.models import Contact,Member
from petcareapp.forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
            username = request.POST['username'],
            password = request.POST['password'],
        ).exists():
            return render(request,'index.html')
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')



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
        return redirect('/show')
    else:
        return render(request,'contact.html')


def pricing(request):
    return render(request,'pricing.html')

def show(request):
    allcontacts=Contact.objects.all()
    return render(request,'show.html',{'contact':allcontacts})

def delete(request,id):
    contacted = Contact.objects.get(id=id)
    contacted.delete()
    return redirect('/show')

def edit(request,id):
    editcontact = Contact.objects.get(id=id)
    return render(request,'edit.html',{'contact':editcontact})

def update(request,id):
    updateinfo = Contact.objects.get(id=id)
    form = ContactForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request,'edit.html')

def register(request):
    if request.method == 'POST':
         members = Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password'],
         )
         members.save()
         return redirect('/login')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')