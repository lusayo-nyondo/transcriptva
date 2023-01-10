from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('transcriptva_clientsite/home.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def privacy_policy(request):
    template = loader.get_template('transcriptva_clientsite/privacy_policy.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def terms_and_conditions(request):
    template = loader.get_template('transcriptva_clientsite/terms_and_conditions.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def services(request):
    template = loader.get_template('transcriptva_clientsite/services.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def automated_transcription_service(request):
    template = loader.get_template('transcriptva_clientsite/services/automated_transcription.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def manual_transcription_service(request):
    template = loader.get_template('transcriptva_clientsite/services/manual_transcription.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def faq(request):
    template = loader.get_template('transcriptva_clientsite/faq.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def tools(request):
    template = loader.get_template('transcriptva_clientsite/tools.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))
