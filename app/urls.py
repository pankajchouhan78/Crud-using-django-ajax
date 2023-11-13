from . import views
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('save/',views.save_data,name="save"),
    path('delete/',views.delete_data,name="delete"),
    path('edit/',views.edit_data,name="edit"),
]
