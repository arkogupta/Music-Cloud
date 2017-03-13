'''

from django.shortcuts import render, get_object_or_404
from django.http import  Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums' : all_albums})
    #template = loader.get_template('music/index.html')
    #context = { 'all_albums' : all_albums}
    #all_albums is the table we require
    #we make a dictionary called context using this
    #return HttpResponse(template.render(context,request)) #return httpresponse as the html template
    # shorter way of returning reponse



def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
    # album = get_object_or_404(Album, pk= album_id) ->shortcut for try..except


#    try:
        #album = Album.objects.get(pk = album_id)
    #except Album.DoesNotExist:
     #   raise Http404("Album does not exist")



def favourite(request , album_id):
    album = get_object_or_404(Album , pk = album_id)

    try:
        sel_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError):
        return  render(request , 'music/detail.html' ,{'album' : 'album' ,'error_message' : 'You did not select a valid song'})


    else:
        sel_song.is_fav = True
        sel_song.save()
        return render(request , 'music/detail.html' , {'album' : album })
'''

from django.views import  generic
from .models import  Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'


    def get_queryset(self):
        return  Album.objects.all()




class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'



















