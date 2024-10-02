from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Images, Clients, Franchise, Enquiry, Products, Machines, Credentials
# Create your views here.

def home(request):
    images = Images.objects.all()
    clients = Clients.objects.all()
    brands = Franchise.objects.all()

    return render(request, 'home/index.html',{'images':images,'clients':clients,'brands':brands})

def about(request): 
    images = Images.objects.all()
    return render(request, 'home/about.html',{'images':images})

def privacy(request): 
    images = Images.objects.all()
    return render(request, 'home/privacy.html',{'images':images})

def product(request, id):
    products = Products.objects.filter(id=id)
    images = Images.objects.all()
    if id <= 9:
        machines = Machines.objects.filter(category = "packaging")
        credentials = Credentials.objects.filter(category = "packaging")
    if id >= 10 and id <= 17:
        machines = Machines.objects.filter(category = "wpc")
        credentials = Credentials.objects.filter(category = "wpc")
    if id >= 18:
        machines = Machines.objects.filter(category = "hdpe")
        credentials = Credentials.objects.filter(category = "hdpe")
    
    return render(request, 'home/individual.html',{'products':products,'machines':machines,'credentials':credentials,'images':images})


def contact(request):
    if request.method == "POST":
        #print(request)
        name = request.POST.get("name",'default')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        msg = request.POST.get("msg",'')
        #print(name, email, phone, desc)
        #saving contact in databse
        contact = Contact(name =name, email = email, phone = phone, msg = msg)
        contact.save() #IMP LINE
    return render(request, 'home/contact.html')

def enquiry(request):
    if request.method == "POST":
        #print(request)
        name = request.POST.get("name",'default')
        last = request.POST.get("last",'default')
        product = request.POST.get('product','')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        msg = request.POST.get("msg",'')
        #print(name, email, phone, desc)
        #saving contact in databse
        enquiry = Enquiry(name =name, last= last, product_name= product, email = email, phone = phone, msg = msg)
        enquiry.save() #IMP LINE
    return render(request, 'home/enquiry.html')

