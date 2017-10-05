from django.shortcuts import render
from coolapp.models import Users, Film, Weather
from coolapp.forms import FilmForm, CommentsForm
from django.shortcuts import redirect
from coolapp.tasks import send_email


# Create your views here.
from django.http import HttpResponse


def films(request):
    obj = Film.objects.all()
    last = Weather.objects.order_by("-id")[0:1]
    weather = last[0]
    return render(request, 'coolapp/films.html', {'Films': obj, 'Weather': weather})


def film(request, film_id):
    f = Film.objects.get(id=film_id)
    u = Users.objects.get(id=f.user_id_id)
    if request.method == 'POST':
        commentsform = CommentsForm(request.POST)
        if commentsform.is_valid():
            comments = commentsform.save(commit=False)
            comments.film_id = f
            comments.save()
            return redirect('/index/{}'.format(f.id), comments=comments)
    else:
        commentsform = CommentsForm()
        return render(request, 'coolapp/film.html', {'film': f, 'user': u, 'commentsform': commentsform})


def index(request):
    return render(request, 'coolapp/index.html')


def add_film(request):
    if request.method == 'POST':
        filmform = FilmForm(request.POST)
        if filmform.is_valid():
            film = filmform.save()
            user = Users.objects.filter(id=film.user_id_id)
            print(user[0].email)
            send_email(user[0])

            return redirect('/index/{}'.format(film.id), film=film)
    else:
        filmform = FilmForm()
        return render(request, 'coolapp/add_film.html', {'filmform': filmform})
