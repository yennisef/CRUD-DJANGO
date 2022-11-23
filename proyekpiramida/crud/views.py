from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TableMobil

class IndexMobil(ListView):
    queryset = TableMobil.objects.all()

class TambahMobil(CreateView):
    model=TableMobil
    fields='__all__'
    success_url=reverse_lazy('mobil:index')