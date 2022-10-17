from django.urls import path

from pessoas import views

urlpatterns = [path("", views.index, name="pessoas")]
