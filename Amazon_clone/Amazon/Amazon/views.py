from django.shortcuts import render
from products_data import side_bar_data
def home(request):
    return render(request, 'home.html',{"data": side_bar_data.menu_data})