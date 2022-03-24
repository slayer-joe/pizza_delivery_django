from django.urls import path
from .views import ActionList

urlpatterns = [
    path('', ActionList.as_view(), name="actions"),
]
