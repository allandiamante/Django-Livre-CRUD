from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, Atividade, Status, Classe, Campus 
from django.urls import reverse_lazy
from django.views.generic.list import ListView
# Create your views here.

############# CREATE #############

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao' ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class CampusCreate(CreateView):
    model = Campus
    fields = ['nome', 'nivel', 'descricao' ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


############# UPDATE #############

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


############# DELETE #############

class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

############# LIST #############

class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    
class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
   