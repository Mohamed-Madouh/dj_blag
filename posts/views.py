from django.shortcuts import render , redirect
from .models import post
from .forms import postfrom
# Create your views here.
def all_posts(requset):
    posts = post.objects.all()
    return render(requset, 'posts.html',{'mohamed':posts}  )
def single_post(requset,id):
    post1 = post.objects.get(id=id)
    return render(requset, 'single.html', {'single_post':post1})
def new_post  (requset):
    if requset.method =='POST':
        form = postfrom(requset.POST)
        if form.is_valid():
            form.save()
    else:
        form = postfrom()
    return render(requset, 'new.html',{'form': form})
    


def Edit_post  (requset,id ):
    post1 = post.objects.get(id=id)
    if requset.method =='POST':
        form = postfrom(requset.POST)
        if form.is_valid():
            form.save()
    else:
        form = postfrom(instance=post1)
    return render(requset, 'edit.html',{'form': form})
 
 
def delete_post (requset,id):
    post1 = post.objects.get(id=id) 
    post1.delete()
    return redirect('/blag/')
