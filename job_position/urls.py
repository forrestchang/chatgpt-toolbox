from django.urls import path

from . import views

app_name = "job_position"

urlpatterns = [path("", views.job_position_index, name="job_position_index")]
