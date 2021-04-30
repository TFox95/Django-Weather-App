from django.urls import path
from . import views
#We created this file because this file will tell Django
#that if we open up this url it's going to run a Function
#called index from the views py file
urlpatterns = [
    path("", views.index),
]
