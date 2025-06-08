from django.contrib import admin
from .models import EthischeFrage, SpielerAntwort, TheorieText, AntwortBewertung

admin.site.register(EthischeFrage)
admin.site.register(SpielerAntwort)
admin.site.register(TheorieText)
admin.site.register(AntwortBewertung)
