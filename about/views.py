from django.shortcuts import render

# Create your views here.
def myself(request):
    return render(request, 'about/myself.html')