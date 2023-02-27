from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from .models import Notes
from django.contrib.auth.decorators import login_required

# from my_todo.forms import NotesForm

@login_required
def Home(request):
    user_notes=Notes.objects.filter(user=request.user)
   
    return render(request,'home.html', {
        'user_notes':user_notes,
    })
   
@login_required
def Add_notes(request):
    if request.method=='POST':
        note=request.POST.get('note')
        user=request.user
        print(user)
        my_notes=Notes.objects.create(user=user,note=note)
        my_notes.save()
        # print(note)
    
    return redirect('home')
@login_required
def Delete_note(request,pk):
    note = get_object_or_404(Notes, pk=pk)
    # post_pk = comment.post.pk
    note.delete()   
    return redirect('home')
  

def SignupPage(request):
    
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('psw')
        pass2=request.POST.get('psw-repeat')
        if pass1 != pass2:
            return HttpResponse("password1 and password2 not equal ")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("login")
        # print(uname," ",email," ",pass1," ",pass2)
        
    return render(request,'signup.html')
@csrf_protect
def LoginPage(request):
    if request.method=="POST": 
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            
        else:
            return HttpResponse("invalid User")
            ...
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



# def add_note(request,pk):
    