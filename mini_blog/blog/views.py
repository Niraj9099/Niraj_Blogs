from django.shortcuts import render, HttpResponseRedirect
from .form import UserCreateForm, Addpost, Contact_Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import blog_model
from django.contrib import messages
from django.core.cache import cache
from django.views.generic import DetailView
# paginater in django
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = blog_model.objects.all().order_by('id')[::-1]
    paginator = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'data':page_obj})

class PostDetail(DetailView):
    model = blog_model
    template_name = 'blog/post.html'

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        fm = Contact_Form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Message was Successfully send !!!')
            fm = Contact_Form()
    else:
        fm = Contact_Form()
    return render(request, 'blog/contact.html', {'form':fm})

def Signup_form(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserCreateForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Account Created SuccessFully !!!')
                fm = UserCreateForm()
        else:
            fm = UserCreateForm()
        return render(request, 'blog/singup.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashbord/')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                user = authenticate(username=nm, password=pw)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashbord/')
        else:
            fm = AuthenticationForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashbord/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashbord_page(request):
    if request.user.is_authenticated:
        super = request.user.is_superuser
        if super:
            data = blog_model.objects.all()
        else:
            data = blog_model.objects.filter(user__id = request.user.id)
        user = request.user
        
        full_name = user.get_full_name()

        ip = request.session.get('ip', 0)
        cp = cache.get('count', 0, version=user.pk)
        return render(request, 'blog/dashbord.html', {'name': full_name, 'data':data, 'super':super, 'ip':ip, 'cp':cp})
    else:
        return HttpResponseRedirect('/login/')

def delete_data(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = blog_model.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Blog Deleted SuccessFully !!!')
            return HttpResponseRedirect('/dashbord/')
    else:
        return HttpResponseRedirect('/login/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ap = Addpost(request.POST, request.FILES)
            if ap.is_valid():
                user_id = request.user.id
                print('user_id : ', user_id)
                title = ap.cleaned_data['title']
                disc = ap.cleaned_data['disc']
                img = ap.cleaned_data['img']
                data = blog_model(user_id=user_id, title=title, disc=disc, img=img)
                data.save()
                messages.success(request, 'New Blog Created SuccessFully !!!')
                ap = Addpost()
        else:
            ap = Addpost()
        return render(request, 'blog/addpost.html', {'form':ap})
    else:
        return HttpResponseRedirect('/login/')


def adit_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = blog_model.objects.get(pk=id)
            ap = Addpost(request.POST,  request.FILES, instance=pi)
            if ap.is_valid():
                ap.save()
                messages.success(request, 'New Blog Created SuccessFully !!!')
                ap = Addpost()
        else:
            pi = blog_model.objects.get(pk=id)
            ap = Addpost(instance=pi)
        return render(request, 'blog/addpost.html', {'form':ap})
    else:
        return HttpResponseRedirect('/login/')

