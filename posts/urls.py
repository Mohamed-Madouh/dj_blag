from django.urls import path
from .views import all_posts , single_post , Edit_post , delete_post , new_post
urlpatterns = [
    path('', all_posts , name = 'all_posts'),
    path('<int:id>', single_post, name ='single_post'),
    path('new', new_post , name = 'new_posts'),
    path('<int:id>/edit', Edit_post, name ='Edit_post'),
    path('<int:id>/delete', delete_post, name ='delete_post'),
    
]