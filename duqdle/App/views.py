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
    all_songs = Song.objects.values_list('title', flat=True)
    print(all_songs)
    if sotd_dict['title'] not in all_songs:
        print(f"Adding {sotd_dict['title']} - {sotd_dict['artist']}")
        sotd = Song.objects.create(title=sotd_dict['title'],
                                artist=sotd_dict['artist'],
                                image=sotd_dict['image'],
                                # audio_file=sotd_dict['audio_file'],
                                audio_link=sotd_dict['audio_link'])
        sotd.save()
    
    return render(request,"index.html",context)