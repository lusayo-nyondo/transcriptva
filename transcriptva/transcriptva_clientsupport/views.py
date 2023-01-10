from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse


def support(request):
    if not request.user.is_authenticated:
        return redirect('clienthub')
    
    template = loader.get_template('transcriptva_client_webapp/support/index.dtl.html')
    context = {}

    return HttpResponse(template.render(
        context,
        request
    ))
