from django.urls import path
from .views import CompaniesView, CompanyDetailView, EmployeeView, EmployeeEditView, EmployeeContactEditView

urlpatterns = [
    path('', CompaniesView.as_view(), name='companies'),
    path('<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    path('<int:company_id>/<int:employee_id>', EmployeeView.as_view(), name='employee'),
    path('<str:company_id>/<int:employee_id>/edit', EmployeeEditView.as_view(), name='employee_edit'),
    path('<str:company_id>/<int:employee_id>/<int:contact_id>/edit', EmployeeContactEditView.as_view(),
         name='employee_contact_edit'),

]
