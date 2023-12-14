from django.shortcuts import get_object_or_404, render

from .forms import FillingForm


#from ice_cream.models import IceCream


def filling(request):
    form = FillingForm(request.GET or None)
    return render(request, 'filling/filling.html',{'form':form})
