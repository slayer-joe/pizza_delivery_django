from django.views.generic import ListView
from .models import Contact

class ContactsList(ListView):
    paginate_by = 20
    model = Contact
    template_name = 'contacts.html'

