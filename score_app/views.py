from django.shortcuts import render
# diplay the list of people who will participate in the marathon
from .models import Participants

# Create your views here.
def index(request):
    return render(request, 'score_app/index.html',{
    'score_app': Participants.objects.all()
    }) 
