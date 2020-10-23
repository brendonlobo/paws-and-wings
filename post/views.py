from django.shortcuts import render,redirect,get_object_or_404
from .models import memory,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy


# Create your views here.
@login_required(login_url = '/login')
def show_post(request):
    if request.method == 'POST':
        data = request.POST['post']
        image = request.FILES['image']
        new_post = memory(content= data,user=request.user,image=image)
        new_post.save()
        return render(request,"main_page.html")
    else:
        memories = memory.objects.all()
        #for i in memories:
          #  print(i.likes.count())
        return render(request, "main_page.html",{'memories':memories,})

@login_required(login_url = '/login')
def add_post(request):
    if request.method == 'POST':
        data = request.POST['post']
        image = request.FILES['image']
        new_post = memory(content= data,user=request.user,image=image)
        new_post.save()
        return redirect(show_post)
    else:
        return render(request,"upload_post.html")
    
@login_required(login_url = '/login')
def user_profile(request):
    login_user = request.user
    memories = memory.objects.filter(user=login_user)
    return render(request,'profile.html',{'memories':memories})

@login_required(login_url = '/login')
def like(request,pk):
    memories = memory.objects.get(id=pk)
    memories.likes.add(request.user)
    return HttpResponseRedirect(reverse('post'))

@login_required(login_url = '/login')
def post_detail(request,pk):
    if request.method == 'POST':
        comments = request.POST['comment']
        memories = memory.objects.get(id=pk)
        new_comments = Comment(name=request.user,body=comments,post=memories)
        new_comments.save()
        memories = memory.objects.get(id=pk)
        return render(request,'post_detail.html',{'memories':memories})
    else:
        memories = memory.objects.get(id=pk)
        return render(request,'post_detail.html',{'memories':memories})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')