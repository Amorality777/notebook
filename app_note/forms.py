from django.forms import ModelForm
from .models import EmployeesModel, ContactsModel, CompaniesModel


class EmployeesForm(ModelForm):
    class Meta:
        model = EmployeesModel
        fields = ['last_name', 'first_name', 'middle_name']


class ContactsForm(ModelForm):
    class Meta:
        model = ContactsModel
        fields = ['contact_type', 'data']


class CompaniesForm(ModelForm):
    class Meta:
        model = CompaniesModel
        fields = '__all__'
