from django.shortcuts import render, redirect
from home.models import Room, Message

# Create your views here.
def index(request):
    if request.method=="POST":
        username = request.POST.get("username")
        room = request.POST.get("room")
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('message', room_name=room, username=username)
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('message', room_name=room, username=username)
    return render(request, 'index.html')

def MessageView(request,room_name, username):
    get_room= Room.objects.get(room_name=room_name)
    if request.method=="POST":
        message = request.POST.get('message')
        new_message  = Message(room=get_room, message=message, sender=username)
        new_message.save()
    get_message = Message.objects.filter(room=get_room)

    context = {
        "messages" : get_message,
        "user" : username
    }
    return render(request, 'message.html', context)
