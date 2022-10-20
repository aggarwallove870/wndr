from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from wndrland_app.views import *


urlpatterns = [
    # path('',start_page ,name = 'start-page'),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('vision', vision, name='vision'),
    path('contact', contact, name='contact'),
    path('teams', teams,name='teams'),
    path('landingpage', landingpage,name='landingpage'),
    path('video_trailer', video_trailer, name='video_trailer'),

    path('video_demo', video_demo, name='video_demo'),
    path('video_url',video_url,name="video_url"),


     path('test',test,name="test")


]