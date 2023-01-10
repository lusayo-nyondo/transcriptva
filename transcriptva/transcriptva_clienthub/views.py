from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from django.shortcuts import redirect

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .models import (
    User,
    Order,
    Transcript,
    ServicePrice,
    Notification,
    DashboardPost
)

def index(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    template = loader.get_template('transcriptva_clienthub/home/index.dtl.html')
    
    context = {
        'user': request.user,
        'notifications': [],
        'dashboard_posts': []
    }

    notifications = Notification.objects.all()
    dashboard_posts = DashboardPost.objects.all()

    context['notifications'] = notifications
    context['dashboard_posts'] = dashboard_posts

    return HttpResponse(template.render(
        context,
        request
    ))

def notifications(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    
    template = loader.get_template('transcriptva_clienthub/home/notifications.dtl.html')
    context = {
        'notifications': []
    }

    notifications = Notification.objects.all()

    context['notifications'] = notifications

    return HttpResponse(template.render(
        context,
        request
    ))

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

def orders_list(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/orders/list.dtl.html')    
    context = {
        'orders': []
    }

    orders = Order.objects.all()

    context['orders'] = orders

    return HttpResponse(template.render(
        context,
        request
    ))

def order_transcript(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    service_prices = ServicePrice.objects.all()
    price_list = serializers.serialize('json', service_prices)

    if request.method == 'POST':
        fields = request.POST
        files = request.FILES

        file = files['file_input']
        duration = fields['duration']

        type = fields['transcript_type_input'].upper()
        accent = fields['accent_input'].upper()
        verbatim = fields['verbatim_type_input'].upper()
        speaker_identification = fields['speaker_identification_input'].upper()
        number_of_speakers = fields['number_of_speakers_input'].upper()
        timestamping = fields['timestamping_input'].upper()
        
        notes = fields['notes_input']
        amount_due = fields['amount_due']

        # ORDER PRICE AND DURATION ARE ALWAYS RE-CHECKED BEFORE SUBMITTING THE ORDER
        order = Order.objects.create()

        order.owner = request.user

        order.file = file
        
        order.type = type
        order.accent = accent
        order.verbatim = verbatim
        order.number_of_speakers = number_of_speakers
        order.speaker_identification = speaker_identification
        order.timestamping = timestamping
        
        order.notes = notes
        
        order.duration = duration
        order.amount_due = amount_due

        order.save()

        redirect_url = 'view_order/{}'.format(
            order.pk
        )

        return redirect(redirect_url)
    else:
        template = loader.get_template('transcriptva_clienthub/orders/order.dtl.html')
        context = {
            'price_list': price_list,
        }

        return HttpResponse(template.render(
            context,
            request
        ))

def view_order(request, order_id):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/orders/view.dtl.html')
    context = {
        'order': None,
        'status': None,
        'notification': None
    }

    order = Order.objects.get(
        pk=order_id
    )

    context['order'] = order

    return HttpResponse(template.render(
        context,
        request
    ))

def account(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')
    
    template = loader.get_template('transcriptva_clienthub/account/index.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def transcripts_list(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/transcripts/list.dtl.html')
    context = {
        'transcripts': []
    }

    transcripts = Transcript.objects.all()

    context['transcripts'] = transcripts

    return HttpResponse(template.render(
        context,
        request
    ))

def view_transcript(request, transcript_id):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/transcripts/view.dtl.html')
    context = {
        'transcript': None
    }

    return HttpResponse(template.render(
        context,
        request
    ))

def submit_report(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/reports/index.dtl.html')
    context = {}

    return HttpResponse(
        context,
        request
    )

