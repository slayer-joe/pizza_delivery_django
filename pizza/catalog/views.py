from django.views.generic import ListView
from .models import PizzaModel

class PizzaView(ListView):
    paginate_by = 20
    model = PizzaModel
    template_name = 'catalog.html'

