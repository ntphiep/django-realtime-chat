from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ChatRoom, Mess


# Create your views here.


@login_required
def rooms(request):
    rooms = ChatRoom.objects.all()
    
    context = {
        'rooms': rooms
    }
    
    return render(request, 'chat_room/rooms.html', context)


@login_required
def room(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    mess = Mess.objects.filter(room=room)[0:25]
    
    context = {
        'room': room,
        'mess': mess
    }
    
    return render(request, 'chat_room/chat.html', context)
