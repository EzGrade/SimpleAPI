from django.urls import path

from .views import SimpleRequest

urlpatterns = [
    path('', SimpleRequest.as_view()), ]
