from django.contrib import admin

from .models import (
    User,
    Notification,
    Transcript,
    Order,
    ServicePrice
)


admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Transcript)
admin.site.register(Order)
admin.site.register(ServicePrice)
