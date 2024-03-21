from .models import Review
from django import forms

REVIEW_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text','rating']
        widgets = {
            forms.RadioSelect(
                choices = REVIEW_CHOICES
            )
            
            
        }