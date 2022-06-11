from django.shortcuts import render
from django.http import HttpResponse
from .models import user_registration,login,Library

# Create your views here.
def Register(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        u = request.POST['n3']
        p = request.POST['n4']
        cp = request.POST['n5']
        if p == cp:
            user_reg = user_registration.objects.create(name=a, phn=b)
            user_reg.save()
            login_data = login.objects.create(username=u, password=p)
            login_data.save()
            msg = "Registration successfull"
            return render(request, 'login.html',{'msg':msg})
        else:
            msg = "Password Doesn't match"
            return render(request, 'Registration.html',{'msg':msg})
    else:
        return render(request, 'Registration.html')

def Login(request):
    if request.method == 'POST':
        u = request.POST['n1']
        p = request.POST['n2']
        try:
            data = login.objects.get(username=u)
            if data.password == p:
                return render(request,'dashboard.html')
            else:
                msg = "Username or password incorrect"
                return render(request, 'login.html',{'msg':msg})
        except:
            return HttpResponse("Account Doesn't Exists")
    else:
        return render(request, 'login.html')


def logout(request):
    return render(request,'login.html')

def add(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        book = Library.objects.create(book_id=a,book_name=b,price=c)
        book.save()
        msg = "Added Successfully..!!"
        return render(request,'addbook.html',{'msg':msg,'b':b})
    else:
        return render(request,'addbook.html')


def display(request):
    if request.method == 'GET':
        d = login.objects.all()
        return render(request,'Display.html',{'disp':d})
    # else:
    #     return render(request, 'Display.html')


def delete(request):
    if request.method == 'POST':
        a = request.POST['n1']
        data = Library.objects.filter(book_id=a)
        data.delete()
        msg = "Deleted Successfully"
        return render(request,'Display.html',{'msg':msg})
    else:
        return render(request, 'Display.html')


def search(request):
    if request.method == 'POST':
        a = request.POST['n1']
        data = Library.objects.filter(book_id=a)
        return render(request,'search.html',{'data':data})
    else:
        return render(request, 'search.html')

def dash(request):
    return render(request,'dashboard.html')


