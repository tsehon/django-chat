from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room

# if a user tries to go to this page without being authenticated they will be redirected to the login page
@login_required
def rooms(request):
    rooms = Room.objects.all() # get all the rooms from the database

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})