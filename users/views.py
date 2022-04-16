from django.shortcuts import redirect, render
from .forms import registerForm,UserCreationForm
from django.contrib.auth import authenticate,login

def register(request):
    # print('text')
    # if request.user.is_authenticated:
    #     return redirect('home-page')
    if request.user.is_anonymous:
         if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                form.save()
                new_user = authenticate(username=username,password=password)
                if new_user is not None:
                    login(request,new_user)
                    return redirect("login")
         else:
            form = registerForm()
    else:
        return redirect('login')

    return render(request,'users/register.html',{'form':form})

# def login(request):
#     return render(request,'users/login.html')