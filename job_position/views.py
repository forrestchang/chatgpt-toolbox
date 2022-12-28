from django.shortcuts import render


# Create your views here.
def job_position_index(request):
    return render(request, "base.html")
