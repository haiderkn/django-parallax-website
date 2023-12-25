from django.shortcuts import render

# Create your views here.
def parallax_view(request):
    return render(request, 'home/index.html')