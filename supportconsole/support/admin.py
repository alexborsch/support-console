from django.contrib import admin
from .models import SupportCompany, SupportPriority, SupportStatus
# Register your models here.



class SupportCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'status')


admin.site.register(SupportCompany, SupportCompanyAdmin)
admin.site.register(SupportPriority)
admin.site.register(SupportStatus)

admin.AdminSite.site_header = 'Support console'
admin.AdminSite.site_title = 'Support console'
admin.site.index_title = 'Support console'