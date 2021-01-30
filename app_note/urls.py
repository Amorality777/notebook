from django.urls import path
from .views import CompaniesView, CompanyDetailView, EmployeeView,EmployeeCreateView, EmployeeEditView, EmployeeContactEditView, \
    EmployeeContactCreateView, CompanyCreateView

urlpatterns = [
    path('', CompaniesView.as_view(), name='companies'),
    path('create/', CompanyCreateView.as_view(), name='company_create'),
    path('<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    path('<int:company_id>/employee_create', EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:company_id>/<int:employee_id>', EmployeeView.as_view(), name='employee'),
    path('<str:company_id>/<int:employee_id>/edit', EmployeeEditView.as_view(), name='employee_edit'),
    path('<str:company_id>/<int:employee_id>/<int:contact_id>/edit', EmployeeContactEditView.as_view(),
         name='employee_contact_edit'),
    path('<str:company_id>/<int:employee_id>/create_new_contact', EmployeeContactCreateView.as_view(),
         name='employee_contact_create'),

]
