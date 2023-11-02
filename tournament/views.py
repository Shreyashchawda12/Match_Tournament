from django.shortcuts import render
from .models import Match

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})

