from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .form import *
from .models import BlogUsers
# Create your views here.
def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, "home.html", context)


def loginpage(request):
    
    return render(request, "login.html")
    # if(request.session['username'].exist()):
    #     return 

def login_view(request):
    
    if(request.method == 'POST'):
        username = request.POST["loginUsername"]
        password = request.POST["loginPassword"]
        
        if(BlogUsers.objects.filter(username = username).exists()):
            if(BlogUsers.objects.filter(password = password).exists()):
                context = {}
                context['user1'] = BlogUsers.objects.get(username = username)
                request.session['username'] = context['user1'].username
                # print(request.session['username'])
                return redirect("/blog")
            else:
                return HttpResponse("Password is invalid")
        else:
            return HttpResponse("Username is not exist")    

            
def register_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        birthdate = request.POST['birthdate']

        if(BlogUsers.objects.filter(username = username).exists()):
            return HttpResponse("Username is already exist")
        else:
            newuser = BlogUsers(username = username, password = password, email = email, birthdate = birthdate)
            newuser.save()
            
    return redirect('/blog')

def add_blog(request):
    context = {'form': BlogForm}

    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            # image = request.FILES['image']
            title = request.POST.get('title')
            username = request.session['username']
           
            
            
            if form.is_valid():
                content = form.cleaned_data['content']
                
            
            blog_obj = BlogModel.objects.create(
                user = username, title = title,
                content = content
            )
            
            # print(blog_obj)
            blog_obj.save()
            
            return redirect('/blog/')
    
    except Exception as e:
        print(e)        
    return render(request, "add_blog.html", context)


def blogdetail(request, url):
    info = BlogModel.objects.get(slug = url)
    return render(request, 'blogdetail.html', {'blogdetail' : info})

def deleteblog(request, url):
    blog = BlogModel.objects.get(slug = url)
    blog.delete()
    username = request.session['username']
    blogs = BlogModel.objects.filter(user = username)
    return render(request, 'viewYourBlogs.html', {'yourblogs' : blogs})

def viewBlogs(request):
    username = request.session['username']
    blogs = BlogModel.objects.filter(user = username)
    return render(request, 'viewYourBlogs.html', {'yourblogs' : blogs})

def logoutuser(request):
    logout(request)
    return redirect("/")

def search(request):
    searchval = request.POST.get('search')
    print(searchval)
    
    
    data = {'blogs' : BlogModel.objects.all()}
   
    newarr = {'blogs' : []}
    for x in data['blogs']:
        tit = str(x)
        if((tit.lower()).find(str(searchval).lower())>=0):
            
            # data = {'blogs' : BlogModel.objects.filter(title = x)}
            newarr['blogs'].append(x)
        
        
    # if(BlogModel.objects.filter(title.find(searchval))):
    #     print("match")
    
    return render(request, "home.html", newarr)