import json
import requests

from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor.requests.auth import HTTPBasicAuth

from petcareapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from petcareapp.models import Contact, Member, ImageModel
from petcareapp.forms import ContactForm, ImageUploadForm


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

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def token(request):
    consumer_key = 'LyWGRZ6RvCn6IPax4m55J4r1pD3MGdGVWZSxUXVGvA9nqcUr'
    consumer_secret = 'aW7Hemuaf4Uhzrr6MsRYFwvZGLXwLO3Rglg7hrJgYVmKeyojIEwbHkut8totgXJ0'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")