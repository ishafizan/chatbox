from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    # ----------------------------------------
    # chat
    # ----------------------------------------
    path('chat/create', api.create_chat, name='create_chat'),
