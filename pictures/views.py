from datetime import timezone
from django.shortcuts import redirect, render

from pictures.form import BookForm
from pictures.models import Book

# Create your views here.


def index(request):
    context = {}
    return render(request, "pictures/index.html")


def image_upload(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form_is_valid():
            form.save()
            return redirect("image_list")  # アップロード後に画像一覧にリダイレクト
    else:
        form = BookForm()
        return render(request, "pictures/image.html", {"form": form})


def image_list(request):
    images = Image.object.all()
    return render(request, "pictures/index.html", {"images": images})

def image_delete()
