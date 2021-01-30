from django.contrib import admin
from .models import CompaniesModel, EmployeesModel, ContactsModel, ContactsTypeModel


@admin.register(CompaniesModel)
class CompaniesAdmin(admin.ModelAdmin):
    pass


@admin.register(EmployeesModel)
class EmployeesAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsModel)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsTypeModel)
class ContactsTypeAdmin(admin.ModelAdmin):
    pass
