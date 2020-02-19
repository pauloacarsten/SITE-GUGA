from django import forms
from django.forms import ModelForm

from .models import Pessoas


class PessoasFormulario(ModelForm):
    class Meta:
        model = Pessoas
        fields = "__all__"


