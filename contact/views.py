from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .models import ContactModel

# Create your views here.

def contactformView(request):
    if request.method == 'POST':
        frm = ContactForm(request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['name']
            uemail = frm.cleaned_data['email']
            uask = frm.cleaned_data['ask']
            data = ContactModel(name = uname, email = uemail, ask = uask)
            data.save()
            return HttpResponseRedirect('/contact/posted')
    else:
        frm = ContactForm()
    return render(request, 'contact/mycontact.html', {'form':frm})

def posted(request):
    return render(request, 'contact/contactRequest.html')