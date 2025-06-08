from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import EthischeFrage, SpielerAntwort, TheorieText, AntwortBewertung
from django.contrib.auth.decorators import login_required
from random import choice
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'home.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        if not username:
            return render(request, 'login.html', {'error': 'Name darf nicht leer sein.'})
        
        user, created = User.objects.get_or_create(username=username)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    fragen = EthischeFrage.objects.all()
    theorien = TheorieText.objects.all()
    return render(request, 'dashboard.html', {
        'fragen': fragen,
        'theorien': theorien,
    })

@login_required
def Theorie_detail(request, theorie_id):
    theorie = get_object_or_404(TheorieText, id=theorie_id)
    return render(request, 'theorie_detail.html', {'theorie': theorie})

@login_required
def frage_detail(request, frage_id):
    frage = EthischeFrage.objects.get(id=frage_id)
    bereits_geantwortet = SpielerAntwort.objects.filter(benutzer=request.user, frage=frage).exists()

    if request.method == 'POST':
        text = request.POST['antwort']
        if not bereits_geantwortet:
            SpielerAntwort.objects.create(benutzer=request.user, frage=frage, antwort_text=text)
        return redirect('dashboard')
    
    return render(request, 'frage_detail.html', {'frage': frage, 'bereits_geantwortet': bereits_geantwortet})

@login_required
def antworten_bewerten(request):
    auswahl_antworen = SpielerAntwort.objects.exclude(benutzer=request.user).exclude(antwortbewertung__bewertender=request.user)

    if not auswahl_antworen.exists():
        return render(request, 'antworten_bewerten.html', {'keine_antwort': True})

    antwort = choice(list(auswahl_antworen))

    if request.method == 'POST':
        bewertung = int(request.POST['bewertung'])
        kommentar = request.POST.get('kommentar', '')
        AntwortBewertung.objects.create(
            bewertender=request.user,
            antwort=antwort,
            bewertung=bewertung,
            kommentar=kommentar
        )
        return redirect('antworten_bewerten')

    return render(request, 'antworten_bewerten.html', {'antwort': antwort})

@login_required
def dashboard(request):
    fragen = EthischeFrage.objects.all()
    theorietexte = TheorieText.objects.all()
    return render(request, 'dashboard.html', {
        'fragen': fragen,
        'theorietexte': theorietexte
    })