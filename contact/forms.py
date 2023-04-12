from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        exclude=('date',)
   #     fields='__all__'
  #en vez del all vamos a utilizar un exclude
    #para que nos excluya 

         
        