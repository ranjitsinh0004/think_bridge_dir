from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView
#,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model=Product
    template_name='home.html'
    ordering = ['choice']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')

#########################API##############################
import requests


def get_product_info(request):
    url='http://127.0.0.1:8000/api/productinfo'  #url to be consumed
    response = requests.get(url)
    print('type of response: ',type(response))
    data=response.json() #list
    print('type of data: ',type(data))
    return render(request,'api_home.html',{"data":data})
