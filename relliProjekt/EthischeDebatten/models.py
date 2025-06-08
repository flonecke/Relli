from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class EthischeFrage(models.Model):
    frage_text = models.TextField()
    thema = models.CharField(max_length=200)
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.frage_text[:50]
    
class SpielerAntwort(models.Model):
    benutzer = models.ForeignKey(User, on_delete=models.CASCADE)
    frage = models.ForeignKey(EthischeFrage, on_delete=models.CASCADE)
    antwort_text = models.TextField()
    erstellt_am = models.DateTimeField(auto_now_add=True)

class TheorieText(models.Model):
    title = models.CharField(max_length=200)
    inhalt = models.TextField()
    bezug_frage = models.ForeignKey(EthischeFrage, on_delete=models.SET_NULL, null =True, blank=True)
    
    def __str__(self):
        return self.inhalt[:50]

class AntwortBewertung(models.Model):
    bewertender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bewertungen')
    antwort = models.ForeignKey(SpielerAntwort, on_delete=models.CASCADE)
    kommentar = models.TextField(blank=True)
    bewertung = models.IntegerField(choices=[(1, 'Unvertretbar'), (2, 'Okey'), (3, 'Vertretbar')])