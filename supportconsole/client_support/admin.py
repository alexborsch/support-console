from django.contrib import admin
from .models import SupportTikets, SupportDevelopment
from django.contrib.auth.models import Group

users_in_group = Group.objects.get(name__in=["IEK"]).user_set.all()


class SupportTiketsAdmin(admin.ModelAdmin):
    def get_queryset(self, request, obj=None):
        if request.user in users_in_group:
            qs = super(SupportTiketsAdmin, self).get_queryset(request)
            return qs.filter(created_by=request.user)
        else:
            return super(SupportTiketsAdmin, self).get_queryset(request)

    list_display = ('issue', 'department', 'priority', 'created_at', 'created_by', 'status')
    list_filter = ("created_at", 'priority', 'status')
    search_fields = ("issue", )
    exclude = ('created_by',)

class SupportDevelopmentAdmin(admin.ModelAdmin):
    def get_queryset(self, request, obj=None):
        if request.user in users_in_group:
            qs = super(SupportDevelopmentAdmin, self).get_queryset(request)
            return qs.filter(created_by=request.user)
        else:
            return super(SupportDevelopmentAdmin, self).get_queryset(request)

    list_display = ('issue', 'department', 'priority', 'created_at', 'created_by', 'status')
    list_filter = ("created_at", 'priority', 'status')
    search_fields = ("issue", )
    exclude = ('created_by',)


admin.site.register(SupportTikets, SupportTiketsAdmin)

admin.site.register(SupportDevelopment, SupportDevelopmentAdmin)