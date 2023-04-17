from django.urls import path
from . import views
urlpatterns = [
    path('music', views.all_music, name="listMusic"),
    path('music/create', views.create, name="createMusic"),
    path('music/delete/<int:id>', views.delete, name="deleteMusic")
]