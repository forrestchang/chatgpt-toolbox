from django.urls import path

from . import views

app_name = "chatgpt"

urlpatterns = [path("", views.chatgpt_index, name="chatgpt_index")]
