from django.shortcuts import render
from .models import Sprint
# Create your views here.


def sprinthome(request):
    sprints = Sprint.objects
    return render(request,'sprinthome.html',{'sprints':sprints})
