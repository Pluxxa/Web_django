# main_1/forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'x_position', 'y_position']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Оставьте ваше сообщение здесь...'}),
            'x_position': forms.HiddenInput(),
            'y_position': forms.HiddenInput(),
        }
