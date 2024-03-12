from django import forms
from .models import UserModel

class HospitalForm(forms.ModelForm):
        class Meta :
                model = UserModel
                fields = "__all__"
                