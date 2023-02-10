from django.contrib import admin

from transcriptva_clienthub.models import (
    Transcript,
    Order,
    ServicePrice,
    Notification,
    DashboardPost
)

from transcriptva_clientsupport.models import (
    ClientIssue,
    IssueAttachment
)

from transcriptva_clientaccount.models import (
    User
)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'email', 'first_name', 'last_name', 'is_staff' ]
    search_fields = [ 'username', 'email' ]


@admin.register(ServicePrice)
class ServicePriceAdmin(admin.ModelAdmin):
    list_display = [ 'type', 'verbatim', 'timestamping', 'speaker_identification', 'number_of_speakers', 'price_per_minute' ]
    search_fields = [ 'type', 'verbatim', 'timestamping', 'speaker_identification', 'number_of_speakers' ]

    list_editable = [ 'price_per_minute' ]


@admin.action(description='Queue order for transcription')
def queue_order_for_transcription(modeladmin, request, queryset):
    for order in queryset:
        transcript = Transcript.objects.get_or_create(
            order=order
        )
        
        order.status = 'AWAITING_TRANSCRIPTION'

        transcript.save()
        order.save()

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'owner', 'reference', 'status', 'amount_due', 'created_on' ]
    search_fields = [ 'owner', 'reference', 'status', 'created_on' ]

    list_editable = [ 'status' ]
    actions = [ queue_order_for_transcription ]

admin.site.register(Transcript)
admin.site.register(Notification)
admin.site.register(DashboardPost)


class IssueAttachmentsInline(admin.StackedInline):
    model = IssueAttachment


class ClientIssueAdmin(admin.ModelAdmin):
    inlines = [ IssueAttachmentsInline ]


admin.site.register(ClientIssue, ClientIssueAdmin)
