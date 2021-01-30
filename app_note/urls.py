from django.urls import path
from .views import CompaniesView, CompanyDetailView, EmployeeView

urlpatterns = [
    path('', CompaniesView.as_view(), name='companies'),
    path('<int:company_id>/', CompanyDetailView.as_view(), name='company_detail'),
    path('<int:company_id>/<int:employee_id>', EmployeeView.as_view(), name='employee'),
]
