from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WishList

# Create your views here.
def index(request):
    wish_items = WishList.objects.all()
    return render(request, 'index.html', {
        'wish_items': wish_items
    })

class WishAdd(CreateView):
    model = WishList
    fields = '__all__'
    success_url = '/'