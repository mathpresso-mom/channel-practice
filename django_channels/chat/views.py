# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import transaction
from django.shortcuts import render, redirect

from chat.models import Room


def about(request):
    return render(request, 'chat/about.html')


def new_room(request):
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = str(uuid.uuid4())
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
        return redirect(chat_room, label)


def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages,
    })
