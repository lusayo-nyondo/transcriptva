from django.contrib import admin

from .models import (
    User,
    Transcript,
    Order,
    ServicePrice,
    Notification,
    DashboardPost
)


class UserAdmin(admin.ModelAdmin):
    list_display = [ 'first_name', 'last_name' ]
    search_fields = [ 'username', 'email' ]


admin.site.register(User, UserAdmin)

admin.site.register(Transcript)
admin.site.register(Order)
admin.site.register(ServicePrice)
admin.site.register(Notification)
admin.site.register(DashboardPost)
