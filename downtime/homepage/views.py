from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from filling.models import Downtime, Park, Sample, Equip, Failure_сategory
from django.db.models import Subquery


def index(request):
    failure_list = Downtime.objects.all()
    return render(
        request,
        'homepage/index.html',
        {'failure_list': failure_list}
    )