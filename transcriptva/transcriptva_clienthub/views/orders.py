from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.core import serializers

from django.core.paginator import Paginator

from transcriptva_clienthub.models import (
    Order,
    Transcript,
    ServicePrice,
)

def orders_list(request):
    
    if not request.user.is_authenticated:
        return redirect('clienthub')
    template = loader.get_template('transcriptva_clienthub/orders/list.dtl.html')    
    context = {
        'orders': [],
        'status': None,
        'order_by': None,
        'search_term': None,
        'page': None
    }

    orders = None
    status = 'ALL'
    order_by = 'date_desc'
    search_term = ''
    page = 1

    if request.method == 'GET':
        fields = request.GET

        if 'status' in fields:
            status = fields['status'].upper()
        if 'order_by' in fields:
            order_by = fields['order_by']
        if 'search_term' in fields:
            search_term = fields['search_term'].strip()
        if 'page_num' in fields:
            page = int(fields['page_num'])


    orders = Order.objects.filter(
        owner=request.user
    )
    
    if status != 'ALL':
        orders = orders.filter(status=status)

    if len(search_term) > 0:
        orders = orders.filter(transcript__file__icontains=search_term)

    if order_by == 'date_desc':
        orders = orders.order_by('-created_on')
    elif order_by == 'date_asc':
        orders = orders.order_by('created_on')
    
    paginator = Paginator(orders, 6)

    context['paginator'] = paginator
    context['page_obj'] = paginator.page(page)
    context['orders'] = paginator.page(page).object_list
    context['status'] = status
    context['order_by'] = order_by
    context['search_term'] = search_term
    context['page'] = page

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

        # Create both the order and the transcript object and
        # then send over to the pay for order page to change the status
        # of the order to paid.

        order = Order.objects.create()

        # Order reference is auto-generated
        order.owner = request.user
        
        order.service = order._get_service_by_details(
            type,
            accent,
            verbatim,
            speaker_identification,
            number_of_speakers,
            timestamping
        )

        order.notes = notes
        order.amount_due = amount_due

        transcript = Transcript.objects.create()

        transcript.owner = request.user
        transcript.order = order

        transcript.file = file
        transcript.type = type
        transcript.accent = accent
        transcript.verbatim = verbatim
        transcript.number_of_speakers = number_of_speakers
        transcript.speaker_identification = speaker_identification
        transcript.timestamping = timestamping
        transcript.duration = duration
        transcript.applicable_cost = amount_due

        order.save()
        transcript.save()

        redirect_url = 'make_order_payment/{}'.format(
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

def make_order_payment(request, order_id):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/orders/make_payment.dtl.html')
    context = {
        'order': Order.objects.get(
            pk=order_id
        )
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

def transcripts_list(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')

    template = loader.get_template('transcriptva_clienthub/transcripts/list.dtl.html')
    context = {
        'transcripts': [],
        'status': None,
        'order_by': None,
        'search_term': None,
        'page': None
    }

    transcripts = None
    status = 'ALL'
    order_by = 'date_desc'
    search_term = ''
    page = 1

    if request.method == 'GET':
        fields = request.GET

        if 'status' in fields:
            status = fields['status'].upper()
        if 'order_by' in fields:
            order_by = fields['order_by']
        if 'search_term' in fields:
            search_term = fields['search_term'].strip()
        if 'page_num' in fields:
            page = int(fields['page_num'])


    transcripts = Transcript.objects.filter(
        owner=request.user
    )
    
    if status != 'ALL':
        transcripts = transcripts.filter(status=status)

    if len(search_term) > 0:
        transcripts = transcripts.filter(file__icontains=search_term)

    if order_by == 'date_desc':
        transcripts = transcripts.order_by('-created_on')
    elif order_by == 'date_asc':
        transcripts = transcripts.order_by('created_on')
    
    paginator = Paginator(transcripts, 6)

    context['paginator'] = paginator
    context['page_obj'] = paginator.page(page)
    context['transcripts'] = paginator.page(page).object_list
    context['status'] = status
    context['order_by'] = order_by
    context['search_term'] = search_term
    context['page'] = page

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
