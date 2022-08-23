from django.shortcuts import render
from .models import Album, Songs
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def home(request):
    albums = Album.objects.all()[::-1]

    page = request.GET.get('page')
    paginator = Paginator(albums, 8)
    albums = paginator.get_page(page)
    if request.method == "POST":
        search = request.POST.get("Search")
        albums = Album.objects.filter(
            Q(artist__artist_name__icontains=search) | Q(name__icontains=search))

        if not albums.exists():
            messages.warning(request, "Sorry No Result Found")

    context = {'albums': albums, 'paginator': paginator}
    return render(request, 'music.html', context)


def show(request, pk):
    album = Songs.objects.filter(album=pk)

    data = Album.objects.get(id=pk)
    album_name = data.name
    album_image = data.image

    context = {'album': album, 'album_name': album_name,
               'album_image': album_image}

    return render(request, 'show3.html', context)
