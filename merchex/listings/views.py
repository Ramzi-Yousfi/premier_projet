from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from listings.models import Band
from listings.form_contact import ContactUsForm ,BandForm
from django.shortcuts import redirect  
from django.core.mail import send_mail

# ajoutez cet import
# Create your views here.

def band_list(request):
    bands  = Band.objects.all()
    return render (request,'listings/band_list.html',context ={"bands":bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                    'listings/band_detail.html',
                    {'band':band})
	
def about(request):
    return render(request,'listings/about.html')
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
           send_mail(
             subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
             message=form.cleaned_data['message'],
                 from_email=form.cleaned_data['email'],
             recipient_list=['admin@merchex.xyz'],
        )

        return redirect("email-envoyer")

    else:
        form = ContactUsForm()
    
    return render(request,
                  'listings/contact.html',
                  {'form':form})
def email_send(request):
    return render(request,"listings/email_send.html")

def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else: form =BandForm()
    return render(request,'listings/band_create.html',{'form':form})