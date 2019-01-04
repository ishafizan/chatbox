# -*- coding: utf-8 -*-
from django.urls import path
from . import api

urlpatterns = [
    # ----------------------------------------
    # chat
    # ----------------------------------------
    path('create/', api.create_chat, name='create_chat'),
    # path('chat/view/', api.list_chat, name='list_chat'),
    # path('chat/edit/', api.edit_chat, name='edit_chat'),
    # path('chat/delete/', api.delete_chat, name='delete_chat'),

]
