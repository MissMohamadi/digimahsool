from django.shortcuts import render,redirect,HttpResponse

from .models import Product

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import User

from .forms import SignUpForm,UpdateUserForm

from .models import Category


def helloworld(request):

    all_products = Product.objects.all()

    return render(request,'index.html',{'products':all_products})

def NewYear(request):

    all_products = Product.objects.filter(category=2)

    return render(request,'NewYear.html',{'products':all_products})

def FreeDelivery(request):

    all_products = Product.objects.filter(category=1)

    return render(request,'FreeDelivery.html',{'products':all_products})

def Bellow200(request):

    all_products = Product.objects.filter(category=3)

    return render(request,'Bellow200.html',{'products':all_products})

def JanebiPc(request):

    all_products = Product.objects.filter(category=4)

    return render(request,'JanebiPc.html',{'products':all_products})

def Behdashti(request):

    all_products = Product.objects.filter(category=5)

    return render(request,'Behdashti.html',{'products':all_products})
def NewTechnology(request):

    all_products = Product.objects.filter(category=6)

    return render(request,'NewTechnology.html',{'products':all_products})

def PetFood(request):

    all_products = Product.objects.filter(category=7)

    return render(request,'PetFood.html',{'products':all_products})

def Pushak(request):

    all_products = Product.objects.filter(category=2)

    return render(request,'Pushak.html',{'products':all_products})

def Stationary(request):

    all_products = Product.objects.filter(category=9)

    return render(request,'Stationary.html',{'products':all_products})

def Laptop(request):

    all_products = Product.objects.filter(category=10)

    return render(request,'Laptop.html',{'products':all_products})

def Office(request):

    all_products = Product.objects.filter(category=11)

    return render(request,'Office.html',{'products':all_products})

def GamingMonitor(request):

    all_products = Product.objects.filter(category=12)

    return render(request,'GamingMonitor.html',{'products':all_products})

def Login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            # return redirect('index')
            return redirect('helloworld')
        else:
            messages.error(request,'نام کاربری و یا رمز عبور نادرست است')
            return redirect('Login')

    else:

        return render(request, 'login.html')

def signup(request):

    form = SignUpForm()

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, ('ثبت نام شما با موفقیت انجام شد'))
            return redirect('helloworld')

        else:
            messages.error(request, ('ثبت نام شما انجام نشد'))
            # messages.error(request, form.errors)     نمایش خطاهادر ثبت نام
            return redirect('signup')

    else:
        return render(request, 'signup.html', {'form': form})

def resetPassword(request):

    return render(request,'resetPassword.html')

def category_summary(request):

    all_cat = Category.objects.all()

    return render(request,'category_summary.html',{'category': all_cat})

def category(request , cat):

    cat = cat.replace("-"," ")

    # try:
    category = Category.objects.get(name=cat)
    products = Product.objects.filter(category=category)
    return render(request,'category.html',{'products': products, 'category': category})
    # except:
    #     messages.error(request,'(دسته بندی مورد نظر وجود ندارد)')
    #     return redirect('home')

def logout(request):

    logout(request)

    messages.success(request,("با موفقیت خارج شدید"))

    return redirect("home")