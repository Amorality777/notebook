from django.db import models


class CompaniesModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'companies'


class EmployeesModel(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=25, default=None, null=True, blank=True, verbose_name='Отчество')
    company = models.ForeignKey('CompaniesModel', on_delete=models.CASCADE, related_name='employees',
                                verbose_name='Компания')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'employees'


class ContactsModel(models.Model):
    contact_type = models.ForeignKey('ContactsTypeModel', on_delete=models.CASCADE, related_name='contacts',
                                     verbose_name='Вид связи')
    data = models.CharField(max_length=50, verbose_name='Контактная информация')
    employee = models.ForeignKey('EmployeesModel', on_delete=models.CASCADE, related_name='contacts',
                                 verbose_name='Сотрудник')

    def __str__(self):
        return f'{self.contact_type} {self.employee}'

    class Meta:
        db_table = 'contacts'
        ordering = ['contact_type']


class ContactsTypeModel(models.Model):
    contact_type = models.CharField(max_length=30, verbose_name='Вид связи')

    def __str__(self):
        return self.contact_type

    class Meta:
        db_table = 'contacts_type'
