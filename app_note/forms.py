from django.forms import ModelForm, ModelChoiceField
from .models import EmployeesModel, ContactsModel


class EmployeesForm(ModelForm):
    class Meta:
        model = EmployeesModel
        fields = '__all__'
