from django.contrib import admin
from inoutboard.inoutboard.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    ordering = ('last_name',)
    fields = ('first_name', 'last_name', 'phone',)

admin.site.register(Employee, EmployeeAdmin)
