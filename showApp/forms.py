from django import forms
from showApp.models import Movie,Show


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieUpdateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name','released_date','language')

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('name','age','movie_name','show_time','theater','seats')
