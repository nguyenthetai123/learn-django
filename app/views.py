from django.shortcuts import render
from app.models import slider, banner_area, Main_Category,Product
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def index(request):
    product= Product.objects.filter(section__name='Top Deals Of The Day')
    sliders= slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    main_category= Main_Category.objects.all().order_by('-id')
    context={
        'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
        'product':product
    }
    return render(request, 'index.html', context)

def PRODUCT_DEATIL(request,slug):
    sliders= slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    main_category= Main_Category.objects.all().order_by('-id')
    
    product=Product.objects.filter(slug=slug)
    if product.exists():
        product=Product.objects.get(slug=slug)
    else:
        return redirect('url_not_found')
    context={
         'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
        'product':product
    }
    return render(request, 'product_detail.html', context)
def url_not_found(request):
    return render(request, '_404.html',)

def my_accounts(request):
    return render(request, 'account\my_account.html')

def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request,'username id already exists')
            return redirect('my_account')
        if User.objects.filter(email=email).exists():
            messages.error(request,'email id already exists')
            return redirect('my_account')
        user= User(
            username=username,
            email=email,
            password=password
        )
        user.set_password(password)
        user.save()
    return redirect('my_account')

def LOGIN(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password provided  for login')
            return redirect('my_account')
    return render(request, 'account/my_account.html')

    