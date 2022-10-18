from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('transcriptva_site/home.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def privacy_policy(request):
    template = loader.get_template('transcriptva_site/privacy_policy.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def terms_and_conditions(request):
    template = loader.get_template('transcriptva_site/terms_and_conditions.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def services(request):
    template = loader.get_template('transcriptva_site/services.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def automated_transcription_service(request):
    template = loader.get_template('transcriptva_site/services/automated_transcription.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def manual_transcription_service(request):
    template = loader.get_template('transcriptva_site/services/manual_transcription.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def support(request):
    template = loader.get_template('transcriptva_site/support.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))

def tools(request):
    template = loader.get_template('transcriptva_site/tools.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))
