from django.shortcuts import render, redirect
from .models import Show
from django.utils import timezone
from django.contrib import messages
import pytz

def index(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request,'application/index.html', context)

def display_add_show(request):
    return render(request, 'application/addshow.html')

def addshow(request):
    # print(request.POST['release_date'])
    # print('**************************************')
    errors = Show.objects.validate(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        newshow = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        print(Show.objects.all().values())
        return redirect('/shows/'+str(newshow.id))

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')

def edit(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show_info': show
    }
    return render(request, 'application/editshow.html', context)

def update(request, id):
    errors = Show.objects.validate(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/edit/'+str(id))
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.save()
        show.network = request.POST['network']
        show.save()
        show.release_date = request.POST['release_date']
        show.save()
        show.description = request.POST['description']
        show.save()
        print(Show.objects.all().values())
        return redirect('/shows/'+str(id))

def show(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'application/show.html', context)
