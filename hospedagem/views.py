from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Hospedagem
from .forms import HospedagemForm

class HospedagemList(ListView):
    model = Hospedagem
    template_name = 'hospedagem/hospedagem.html'
    context_object_name = 'hospedagens'

class HospedagemCreate(CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'hospedagem/form.html'
    success_url = reverse_lazy('hospedagem_listar')

class HospedagemUpdate(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'hospedagem/form.html'
    success_url = reverse_lazy('hospedagem_listar')

class HospedagemDelete(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
