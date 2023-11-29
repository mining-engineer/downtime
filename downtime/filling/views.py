from django.shortcuts import get_object_or_404, render

#from ice_cream.models import IceCream


def filling(request):
    return render(request, 'filling/filling.html')
