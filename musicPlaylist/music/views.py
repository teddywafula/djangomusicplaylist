from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Music
from datetime import datetime, date
from django.db.models import Q
from .forms import MusicForm


# Create your views here.


def create(request):
    # if request.POST:
    #     form = MusicForm(request.POST)
    # else:
    #     form = MusicForm()
    # return render(request, 'CreateMusic.html', {'form': form})
    data = Music(
        title="hi",
        link="a test",
        authorName="Teddy",
        createdAt=datetime.now(),
        updatedAt=datetime.now(),
        producedAtDate=date.fromisoformat('2000-01-01')
    )
    data.save()
    return HttpResponseRedirect('/music')
    #
    # template = loader.get_template('CreateMusic.html')
    # context = {
    #     "music": data
    # }
    # return HttpResponse(template.render(context, request))


def all_music(request):
    context = {
        "music": Music.objects.all().values(),
        # "music1": Music.objects.values_list('title'),
        # "music": Music.objects.filter(title__startswith="test").values(),
        # "music": Music.objects.filter(Q(title="test", link="fadf") | Q(title="hi", link="test")).values(),
        # "music": Music.objects.filter(title="hi", link="test").values()
    }
    template = loader.get_template('ListMusic.html')
    return HttpResponse(template.render(context, request))


def delete(request, id):
    item = Music.objects.filter(id=id)
    item.delete()
    return HttpResponse("Item removed successfully")


def details(request, slug):
    music = Music.objects.filter(slug=slug)
    template = loader.get_template('details.html')
    context = {
        "data": music
    }
    return HttpResponse(template.render(context, request))
