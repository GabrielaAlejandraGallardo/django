from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index(request, letter=NULL):
    if letter!=NULL:
        contacts=Contact.objects.filter(name__istartswith=letter)
    else:

    #Dame todos los valores que tenga el search sino existe traeme vacios que es lo mismo que decir traeme
    # el get en el caso que no exista el valor que estamos buscando,coloca el 2do parámetro que es el valor por defecto
         contacts=Contact.objects.filter(name__contains=request.GET.get('search',''))
    context={
        'contacts':contacts
          }
    return render(request,'contact/index.html',context)

def view(request, id):
    contact=Contact.objects.get(id=id)
    context={
        'contact':contact
    }
    return render(request,'contact/detail.html',context)

"""def edit(request, id):
    contact=Contact.objects.get(id=id)

    if request.method== 'GET':
        form=ContactForm(instance=contact)#instance nos permite pasar el contexto de insatancia y abreviar est codigo a continuación (initial={'id':contact.id, 'name':contact.name})
        context={
             'form':form,
              'id':id
              }
        return render(request, 'contact/create.html',context)
    if request.method=="POST":
        form=ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
        context={
             'form':form,
              'id': id
         }
        messages.success(request, 'Contacto actualizado.')
        return render(request, 'contact/create.html',context)    """
def edit(request, id):
    contact=Contact.objects.get(id=id)
    if request.method=='GET':
        form=ContactForm(instance=contact)
        context={
           'form':form,
           'id':id
           }
        return render(request,'contact/edit.html',context)
    if request.method=='POST':
        form=ContactForm(request.POST,instance=contact)
        form.save()
        messages.success(request, 'Contacto actualizado.')
        context={
           'form':form,
           'id':id
           }
        return render(request,'contact/edit.html',context)

      
def create(request):
    if request.method=="GET":
        form=ContactForm()
        context={
             'form':form,
              }
        return render(request, 'contact/create.html',context)    
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid:
            form.save()
        messages.success(request, 'Contacto agregado.')
        return redirect('contact')   
     
def delete(request, id):
    contact=Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')
          