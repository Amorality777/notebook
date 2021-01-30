from django.contrib import admin
from .models import CompaniesModel, EmployeesModel, ContactsModel, ContactsTypeModel


class EmployeesInLine(admin.TabularInline):
    model = EmployeesModel


@admin.register(CompaniesModel)
class CompaniesAdmin(admin.ModelAdmin):
    inlines = [EmployeesInLine]


@admin.register(EmployeesModel)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'company')

    def get_full_name(self, obj):
        if obj.middle_name is not None:
            full_name = f'{obj.last_name} {obj.first_name} {obj.middle_name}'
        else:
            full_name = f'{obj.first_name} {obj.last_name}'
        return full_name

    get_full_name.short_description = 'full name'


@admin.register(ContactsModel)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'data', 'employee')


@admin.register(ContactsTypeModel)
class ContactsTypeAdmin(admin.ModelAdmin):
    pass
