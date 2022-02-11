from django.shortcuts import render, redirect
from showApp.models import Movie,Show
from showApp.forms import MovieForm,MovieUpdateForm, ShowForm
from django.db.models import Max
# Create your views here.

def listMovies(request):
    movies = Movie.objects.all()
    return render(request,'showApp/home.html',{'movies':movies})

def addMovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies')
    return render(request,'showApp/add_movie.html',{'form':form})

def updateMovie(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieUpdateForm(instance=movie)
    if request.method == 'POST':
        form = MovieUpdateForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/movies')
    return render(request,'showApp/update_movie.html',{'form':form})

def deleteMovie(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/movies')

def bookTicket(request,id):
    movie = Movie.objects.get(id=id)
    form = ShowForm()
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ticketDetails')
    return render(request,'showApp/book_ticket.html',{'form':form,'movie':movie})

def ticketDetails(request):
    mid = Show.objects.all().aggregate(Max('id'))
    ticket = Show.objects.get(id=mid['id__max'])
    # if ticket:
    #     return redirect('/ticketDetails'
    return render(request,'showApp/ticket_details.html', {'ticket':ticket})
