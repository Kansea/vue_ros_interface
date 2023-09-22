from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("hello chat")
    return render(request, "chat/index.html")

def room(request, room_name):
    # return HttpResponse("hello room")
    return render(request, "chat/room.html", {"room_name": room_name})
