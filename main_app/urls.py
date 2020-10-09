from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:profile_id>/edit/', views.profile_edit, name='profile_edit'),
    
    path('post/<int:post_id>/', views.post_detail, name='post_detail')
]