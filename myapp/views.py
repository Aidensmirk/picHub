from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
# from datetime import datetime
from .forms import PhotoUploadForm
from .models import Photo

# Create your views here.
# def current_year(request):
#     return {'year': datetime.now().year}

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, 'Photo uploaded successfully!')
            return redirect('home')
    else:
        form = PhotoUploadForm()
    return render(request, 'myapp/upload_photo.html', {'form': form})

def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'myapp/home.html', {'photos': photos})

def about(request):
    return render(request, "myapp/about.html")  

def contact(request):
    return render(request, "myapp/contact.html")  

def gallery(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, "myapp/gallery.html", {"photos": photos})  

def test(request):
    photos = Photo.objects.all()
    return render(request, "myapp/test.html", {"photos": photos})  

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def like_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if request.user in photo.likes.all():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    return redirect('home')