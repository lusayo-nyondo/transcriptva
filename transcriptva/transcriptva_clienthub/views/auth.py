from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from transcriptva_clientaccount.models import (
    User
)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('clienthub')
    
    if request.method == 'POST':
        fields = request.POST

        username = fields['username_input']
        password = fields['password_input']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect('clienthub')
    
    template = loader.get_template('transcriptva_clienthub/auth/sign-in.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))


def sign_out(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    logout(request)

    return redirect('sign_in')

def register(request):
    if request.user.is_authenticated:
        return redirect('clienthub')
    
    if request.method == 'POST':
        fields = request.POST

        username = fields['username_input']
        firstname = fields['firstname_input']
        lastname = fields['lastname_input']
        email = fields['email_input']
        company = fields['company_input']

        password = fields['password_input']
        confirm_password = fields['confirm_password_input']

        # Confirm the user's password here.

        user_fields = {
            'username': username,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password,
            'company': company
        }

        new_user = create_user(user_fields)

        if isinstance(new_user, User):
            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/auth/register.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def create_user(fields):
    user = User.objects.create_user(
        username=fields['username'],
        first_name=fields['firstname'],
        last_name=fields['lastname'],
        email=fields['email'],
        password=fields['password']
    )

    user.save()

    return user
