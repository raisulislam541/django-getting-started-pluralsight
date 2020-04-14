from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .froms import MeetingForm

# Create your views here.
from meetings.models import Meeting, Room


def details(request, id):
    meetings = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/details.html', {"meetings": meetings})


def room_details(request):
    return render(request, 'meetings/rooms.html', {"rooms": Room.objects.all()})


def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')

    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
