from django import forms


class Formulario_comidas(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    price = forms.FloatField()
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)