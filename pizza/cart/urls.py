from django.urls import path
from .views import cart, thankyoupage

urlpatterns = [
    path('', cart, name="cart"),
    path('thankyoupage/', thankyoupage, name="typ")
]
