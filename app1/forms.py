from django import forms
from . models import Product
from . models import Flag
from . models import complete
from . models import Board

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name','style':
            'width: 100%; background:#191919; border-radius: 20px; border: 2px solid #f9004d; min-height:10vh; color:white;'}),
            'description' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Description','style':
            'width: 100%; background:#191919; border-radius: 20px; border: 2px solid #f9004d; min-height:10vh; color:white'}),
            'hint_1': forms.TextInput(attrs={'class': 'form-control'}),
            'flag_1': forms.TextInput(attrs={'class': 'form-control'}),
            'hint_2': forms.TextInput(attrs={'class': 'form-control'}),
            'flag_2': forms.TextInput(attrs={'class': 'form-control'}),
            'hint_3': forms.TextInput(attrs={'class': 'form-control'}),
            'flag_3': forms.TextInput(attrs={'class': 'form-control'}),
            'hint_4': forms.TextInput(attrs={'class': 'form-control'}),
            'flag_4': forms.TextInput(attrs={'class': 'form-control'}),
            'hint_5': forms.TextInput(attrs={'class': 'form-control'}),
            'flag_5': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        fields = ['q1','h1','f1','score']
        widgets = {
            'q1': forms.HiddenInput(),
            'h1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Hint','style':
            'width: 100%; background:#191919; border-radius: 20px; border: 2px solid #f9004d; min-height:10vh; color:white;'}), 
            'f1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Flag','style':
            'width: 100%; background:#191919; border-radius: 20px; border: 2px solid #f9004d; min-height:10vh; color:white;'}),
            'score': forms.Select(attrs={'class': 'regDropDown','placeholder':'Enter Score','style':
            'width: 10%; background:#191919; border-radius: 20px; border: 2px solid #f9004d; min-height:5vh; color:white; text-align: center;'}),
        }

class completeForm(forms.ModelForm):
    model = complete

class BoardForm(forms.ModelForm):
    model = Board