from django import forms 
from .models import Membre, Appointment, Space, Propriete , Receipt


class AppointForm(forms.ModelForm):
    class Meta : 
        model = Appointment
        fields = ('name', 'last_name', 'given_name', 'number','date')
        widgets = {
            'date' : forms.DateInput(attrs={'type':'datetime-local'})
        }



class SpaceForm(forms.ModelForm):
    class Meta : 
        model = Space
        fields  = ('name', 'size', 'title')
       

class ProprieteForm(forms.ModelForm):
    class Meta :
        model = Propriete
        fields = ('user', 'space')

class MembreForm (forms.ModelForm):
    class Meta : 
        model = Membre
        fields = ('name', 'last_name', 'given_name', 'birth', 'address','number','money_GIVE', 'bio','statut','children','infos_children','spouse')
        widgets = {
            'birth' :forms.DateInput(attrs={'type':'date'})
        }

class ReceiptForm(forms.ModelForm):
    class Meta : 
        model = Receipt
        fields = ('title', 'price','user')