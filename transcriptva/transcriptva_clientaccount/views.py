from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import User


def personal_details(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    if request.method == 'POST':
        fields = request.POST

        username= fields['username_input']
        email = fields['email_input']
        firstname =  fields['firstname_input']
        lastname = fields['lastname_input']

        user = User.objects.get(
            pk=request.user.pk
        )

        user.username = username
        user.email = email
        user.first_name = firstname
        user.last_name = lastname

        user.save()
        # User saved successfully, return the page

        context = {
            'status': 'success',
            'message': 'Changes saved successfully.'
        }

        template = loader.get_template('transcriptva_clientaccount/personal/personal_details.dtl.html')
        
        return HttpResponse(template.render(
            context,
            request
        ))
    else:
        template = loader.get_template('transcriptva_clientaccount/personal/personal_details.dtl.html')
        context = {
            'status': None
        }

        return HttpResponse(template.render(
            context,
            request
        ))

def change_password(request):
    if not request.user.is_authenticated:
        redirect('clienthub')

    template = loader.get_template('transcriptva_clientaccount/personal/change_password.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def payment_details(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')
    template = loader.get_template('transcriptva_clientaccount/payment/payment_details.dtl.html')
    context = {
        'status': 'None'
    }

    return HttpResponse(template.render(
        context,
        request
    ))

def delete_account(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clientaccount/personal/delete_account.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

