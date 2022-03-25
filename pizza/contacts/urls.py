from django.urls import path
from .views import ContactsList

urlpatterns = [
    path('', ContactsList.as_view(), name="contacts"),
]
