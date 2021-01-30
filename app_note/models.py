from django.db import models


class CompaniesModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'companies'


class EmployeesModel(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25, default=None, null=True)
    company = models.ForeignKey('CompaniesModel', on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'employees'


class ContactsModel(models.Model):
    contact_type = models.ForeignKey('ContactsTypeModel', on_delete=models.CASCADE, related_name='contacts')
    data = models.CharField(max_length=50)
    employee = models.ForeignKey('EmployeesModel', on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'{self.contact_type} {self.employee}'

    class Meta:
        db_table = 'contacts'


class ContactsTypeModel(models.Model):
    contact_type = models.CharField(max_length=30)

    def __str__(self):
        return self.contact_type

    class Meta:
        db_table = 'contacts_type'
