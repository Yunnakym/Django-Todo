
from django.contrib.auth.forms import UserCreationForm #importe o formulario pronto
from django.urls import reverse_lazy #gera uma resolução preguiçosa, só vai para login se der tudo certo
from django.views import generic #ajuda a criar pagina

class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


