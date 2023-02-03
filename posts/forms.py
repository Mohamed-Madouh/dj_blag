from django import  forms
from .models import post 

class postfrom(forms.ModelForm):
    class Meta :
      model = post 
      fields = ['titel', 'content']