from django.shortcuts import render
from .models import post
# Create your views here.
def all_posts(requset):
    posts = post.objects.all()
    return render(requset, 'posts.html',{'mohamed':posts}  )
def single_post(requset,id):
    post1 = post.objects.get(id=id)
    return render(requset, 'single.html', {'single_post':post1})
    
 
 
 