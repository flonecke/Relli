from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('frage/<int:frage_id>/', views.frage_detail, name='frage_detail'),
    path('antworten_bewerten/', views.antworten_bewerten, name='antworten_bewerten'),
    path('theorie/<int:theorie_id>/', views.Theorie_detail, name='theorie_detail'),
]
