from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('add_post', views.add_post, name='add_post'),
    path('post/<int:post_id>/delete_post', views.delete_post, name='delete_post')
]
