from django import forms
from .models import Res


class StudentForm(forms.ModelForm):
    class Meta:
        model = Res
        fields = "__all__"
