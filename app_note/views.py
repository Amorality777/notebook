from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import CompaniesModel, EmployeesModel


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
