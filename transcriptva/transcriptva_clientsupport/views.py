from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

from .models import (
    ClientIssue,
    IssueAttachment
)

from transcriptva_clienthub.models import Order


def contact_client_support(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    if request.method == 'POST':
        fields = request.POST
        files = request.FILES.getlist('attachments_input')

        mode = fields['mode_input'].upper()
        category = fields['category_input'].upper()
        reference = fields['reference_input']
        notes = fields['notes_input']
        
        client_issue = ClientIssue.objects.create(
            user=request.user,
            mode=mode,
            category=category,
            reference=reference,
            notes=notes
        )

        client_issue.save()

        for file in files:
            issue_attachment = IssueAttachment.objects.create(
                issue=client_issue,
                file=file
            )

            issue_attachment.save()

        context = {
            'mode': 'general',
            'status': 'success',
            'message': 'Your issue has been reported. We will get back to you via email as soon as we can.'
        }

        template = loader.get_template('transcriptva_clientsupport/contact/index.dtl.html')

        return HttpResponse(template.render(
            context,
            request
        ))      
    else:
        template = loader.get_template('transcriptva_clientsupport/contact/index.dtl.html')
        context = {
            'mode': 'general',
            'status': None
        }

        return HttpResponse(template.render(
            context,
            request
        ))


def raise_order_issue(request, order_id):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    order = Order.objects.get(
        id=order_id
    )

    context = {
        'mode': 'order_related',
        'order': order,
        'status': None
    }

    template = loader.get_template('transcriptva_clientsupport/contact/index.dtl.html')

    return HttpResponse(template.render(
        context,
        request
    ))