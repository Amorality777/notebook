from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import CompaniesModel, EmployeesModel, ContactsModel, ContactsTypeModel
from .forms import EmployeesForm


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
        print(employee_form.as_p)
        return render(request, 'app_note/employee_edit.html',
                      context={'employee': employee, 'employee_form': employee_form})

    def post(self, request, company_id, employee_id):
        employee = EmployeesModel.objects.get(id=employee_id)
        employee_form = EmployeesForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee.save()
            return render(request, 'app_note/employee_edit.html',
                          context={'employee': employee, 'employee_form': employee_form})
