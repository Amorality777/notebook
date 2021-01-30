from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import EmployeesForm, ContactsForm
from .models import CompaniesModel, EmployeesModel, ContactsModel


class CompaniesView(ListView):
    model = CompaniesModel
    template_name = 'app_note/companies_list.html'
    context_object_name = 'companies_list'


class CompanyDetailView(View):
    def get(self, request, company_id):
        company = CompaniesModel.objects.get(id=company_id)
        return render(request, 'app_note/company_detail.html', context={'company': company})


class EmployeeView(View):
    def get(self, request, company_id, employee_id):
        employee = EmployeesModel.objects.get(id=employee_id)
        return render(request, 'app_note/employee.html', context={'employee': employee})


class EmployeeEditView(View):
    def get(self, request, company_id, employee_id):
        employee = EmployeesModel.objects.get(id=employee_id)
        employee_form = EmployeesForm(instance=employee)
        return render(request, 'app_note/employee_edit.html',
                      context={'employee': employee, 'employee_form': employee_form})

    def post(self, request, company_id, employee_id):
        employee = EmployeesModel.objects.get(id=employee_id)
        employee_form = EmployeesForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee.save()
            return HttpResponseRedirect(
                reverse('employee', kwargs={'company_id': company_id, 'employee_id': employee_id}))


class EmployeeContactEditView(View):
    def get(self, request, company_id, employee_id, contact_id):
        contact = ContactsModel.objects.get(id=contact_id)
        contact_form = ContactsForm(instance=contact)
        return render(request, 'app_note/employee_contact_edit.html',
                      context={'contact': contact, 'contact_form': contact_form})

    def post(self, request, company_id, employee_id, contact_id):
        contact = ContactsModel.objects.get(id=contact_id)
        contact_form = ContactsForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact.save()
            return HttpResponseRedirect(
                reverse('employee', kwargs={'company_id': company_id, 'employee_id': employee_id}))
