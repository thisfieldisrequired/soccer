from django.shortcuts import render
from .models import Song


def main(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song': song})
