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
        if form.is_valid():
            form.save()
            return redirect(
                "pictures:image_list"
            )  # アップロード後に画像一覧にリダイレクト
    else:
        form = BookForm()
        return render(request, "pictures/image.html", {"form": form})


def image_list(request):
    images = Book.objects.all()
    return render(request, "pictures/index.html", {"images": images})


def image_delete(request, pk):
    image = Book.objects.get(pk=pk)
    image.delete()  # 削除
    return redirect("pictures:image_list")  # 削除後、画像一覧にリダイレクト
