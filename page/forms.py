import this
from django import forms
from .models import *

class Reviewsform(forms.ModelForm):

    

   class Meta:
        # specify model to be used
        model = Reviews
 
        # specify fields to be used
        fields = ['reviewsname','reviewstext','reviewsinstagram']
        
        labels = {'reviewsname':'Фио','reviewstext':'Ваш отзыв','reviewsinstagram':'Ваш инстаграм'}