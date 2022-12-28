from django.shortcuts import render


# Create your views here.
def chatgpt_index(request):
    return render(request, "chatgpt.html")
