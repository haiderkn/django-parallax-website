from django.shortcuts import render

# Create your views here.
def mywork(request):
    return render(request, 'work/mywork.html')