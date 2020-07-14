import datetime

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
#class ReviewForm(forms.Form):
    RATE_CHOICES = [
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
    ]
    name = forms.CharField(label='Автор')
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')
    rating = forms.CharField(label='Оценка:', widget=forms.RadioSelect(choices=RATE_CHOICES))

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
        #exclude = ()

    def clean(self):
        return self.cleaned_data
