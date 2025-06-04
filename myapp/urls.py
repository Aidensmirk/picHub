from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('test/', views.test, name='test'),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
]
