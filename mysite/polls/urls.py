from django.urls import path

from . import views
from . import reset

urlpatterns = [
    path('set', views.index, name='index'),
    path('reset', reset.index, name='index'),
]
