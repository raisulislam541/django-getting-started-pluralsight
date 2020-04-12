from django.http import HttpResponse
from datetime import datetime, timedelta
from django.shortcuts import render

# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"message": Meeting.objects.count()})


def date(request):
    return HttpResponse(f'the page was server at {datetime.now() + timedelta(hours=6)}')


def about(request):
    return HttpResponse('i am raisul islam sajal and i am a junior software developer')
