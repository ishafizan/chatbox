from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    # ----------------------------------------
    # chat
    # ----------------------------------------
    path('api/chat/', include('chat.urls'), name="chat"),

