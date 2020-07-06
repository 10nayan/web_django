from django import forms
from django.forms import ModelForm
from .models import Movie,User
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
CHOICES = [('1', 'First'), ('2', 'Second'),('3','Third')]
class MovieForm(ModelForm):
    class Meta:
        model=Movie
        fields="__all__"
class Task(forms.Form):
    name=forms.CharField(label='Task',max_length=100,widget=forms.TextInput(attrs={'id':'New','class':'form'}))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class':'form'}),
        choices=FAVORITE_COLORS_CHOICES,
    )
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form'}), choices=CHOICES)
    birth_year.widget.attrs.update({'class':'form'})
    def clean_name(self):
        name=self.cleaned_data.get("name")
        if not "play" in name:
            raise forms.ValidationError("Please include play")
        else:
            return name
class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"