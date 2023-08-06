from django.contrib import admin
from api.models import UserModel, PostJobModel
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class JobAdmin(ImportExportModelAdmin):
    list_display = ('company', 'position', 'job_type', 'education', 'experience', 'salary')
    list_filter = ('company', 'position', 'job_type', 'education', 'experience', 'salary')
    search_fields = ('company', 'position', 'job_type', 'education', 'experience', 'salary')

admin.site.register(UserModel)
admin.site.register(PostJobModel, JobAdmin)