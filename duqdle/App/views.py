from django.shortcuts import render, redirect

# Create your views here.
from django.core.paginator import Paginator
from . models import Song
from . helpers import gen_song

def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    sotd_dict = gen_song()
    sotd = Song.objects.create(title=sotd_dict['title'],
                               artist=sotd_dict['artist'],
                               image=sotd_dict['image'],
                               audio_file=sotd_dict['audio_file'])
    sotd.save()
    
    return render(request,"index.html",context)