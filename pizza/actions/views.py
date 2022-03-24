from django.views.generic import ListView
from .models import Action

class ActionList(ListView):
    paginate_by = 10
    model = Action
    template_name = 'action_list.html'

