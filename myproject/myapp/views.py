from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  CustomUser


# Create your views here.
def index(request):
       return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']  # Use 'username' instead of 'name'
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob=request.POST['dob']
        image=request.FILES['image']
        place=request.POST['place']
        print(image)

        
        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            dob=dob,
            place=place,
            image=image
        )

        user.save()
        print(user.image)
        return redirect(index)
    
    return render(request, 'builtinuser.html')

def view(request):
     c=CustomUser.objects.all()
     return render(request,'view.html',{'data':c})





