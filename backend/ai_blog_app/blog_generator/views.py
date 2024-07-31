from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube
# Create your views here.


# idnex function 
@login_required
def index(request):
   return render(request, template_name='index.html')

@csrf_exempt
def generate_blog(request):
   if request.method == "POST":
      try:
         data = json.loads(request.body)
         youtube_link = data['link']
         return JsonResponse({'content':youtube_link})
      except (KeyError, json.JSONDecodeError):
         return JsonResponse({'error':'Inavlid data sent'}, status=400)
      
      #  get title of the video 
      
      title = get_youTube_title(youtube_link)
      # get the transcript of youtueb video 
      
      # used open AI to generate a text blog 
      
      # save blog article to databse
      
      # return blog article as response 
   else:
      return JsonResponse({'error':'Inavlid Request Method'}, status=405)

def get_youTube_title(link):
   yt =YouTube(link)
   title = yt.title
   return title

def user_login(request):
   if request.method =="POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('/')
      else:
         error_message ="User credential is not valid"
         return render(request, template_name='login.html',context={'error_message':error_message})
   return render(request, template_name='login.html')


def user_signup(request):
   if request.method == "POST":
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      confirm_Password = request.POST['confirmPassword']
      
      if password == confirm_Password:
         try:
            if User.objects.filter(username=username).exists():
               error_message = "This Username is already taken"
               return render(request, template_name='signup.html',context={'error_message':error_message})
            
            if User.objects.filter(email = email).exists():
               error_message = "Email already registered"
               return render(request, template_name='signup.html',context={'error_message':error_message})
            
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            login(request,user)
            return redirect(to='/')
         except Exception as e:
            error_message = f"Error Creating Account {e}"
            return render(request, template_name='signup.html',context={'error_message':error_message})
      else:
         error_message = 'Password and Confirm Password does not match'
         return render(request, template_name='signup.html',context={'error_message':error_message})
   return render(request, template_name='signup.html')

def user_logout(request):
   logout(request)
   return redirect('/')