from django import forms


class Formulario_cervezas(forms.Form):
    style = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    alcohol_volume = forms.FloatField()
    IBU = forms.FloatField()
    price = forms.FloatField()
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)
    